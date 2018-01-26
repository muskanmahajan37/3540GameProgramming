import random, sys
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# constants
TIMER_TIME = 33
SIZE = 480
ROTATE_SPEED = 50
TRANSLATE_SPEED = 100

counter = 0

# keep track of which keys are down
keys_down = set()

# state / constants
root_translate = 240.
root_rotate = 45.
ROOT_LENGTH = 200.
ROOT_WIDTH = 20.

seg_rotate = 45.
seg_length = 100.
SEG_WIDTH = 15.

finger_rotate = 45.
FINGER_ROTATE_OFFSET = 45.
FINGER_LENGTH = 25.
FINGER_WIDTH = 5.


# function for drawing a square whose left edge is the y-axis and centered along the y-axis
def drawSquare():
    glBegin(GL_QUADS)
    glVertex2f(0.0, -0.5)
    glVertex2f(1.0, -0.5)
    glVertex2f(1.0,  0.5)
    glVertex2f(0.0,  0.5)
    glEnd()


# function for drawing robot arm
def drawArm():
    global root_translate, root_rotate, seg_rotate, seg_length, finger_rotate, counter



    # TODO: draw the robot arm
    
    # Move arm into position
    glTranslatef(root_translate, ROOT_LENGTH/2, 0);
    #rotate the arm
    glTranslatef(ROOT_WIDTH/2, -ROOT_LENGTH/2, 0);
    glRotatef(root_rotate, 0, 0, -1);
    glTranslatef(-ROOT_WIDTH/2, ROOT_LENGTH/2, 0);
    
    glPushMatrix()
    glScalef(ROOT_WIDTH, ROOT_LENGTH, 1);

    drawSquare();
    glPopMatrix();

    # Move seg into position (relative to arm)
    glTranslatef(SEG_WIDTH/8, (ROOT_LENGTH/2) + (seg_length/2) , 0);
    # rotate the seg
    glTranslatef(SEG_WIDTH/2 , -seg_length/2, 0);
    glRotatef(seg_rotate, 0, 0, -1);
    glTranslatef(-SEG_WIDTH/2 , seg_length/2, 0);
    
    
    glPushMatrix();
    glScalef(SEG_WIDTH, seg_length, 1);
    drawSquare();
    glPopMatrix();
    
    
    glPushMatrix();
    glTranslatef(0, (seg_length/2) + (FINGER_LENGTH/2), 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);
    
    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();
    glPopMatrix(); # firsts finger on the left
    
    
    glTranslatef(0, FINGER_LENGTH, 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(-finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);
    
    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();
    glPopMatrix(); # second finger on the left
    
    glPopMatrix(); # finsihed left fingers

    glTranslatef(SEG_WIDTH - FINGER_WIDTH, (seg_length/2) + (FINGER_LENGTH/2), 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(-finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);

    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();
    glPopMatrix();

    glTranslatef(0, FINGER_LENGTH, 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);

    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();
    glPopMatrix();

    # End TODO

# mouse button handler
def mouseButton(button, state, mx, my):
    global root_translate, root_rotate, seg_rotate, seg_length, finger_rotate

    if button != GLUT_LEFT_BUTTON:
        return

    if state != GLUT_DOWN:
        return

    # TODO: inverse kinematics for robot arm to reach clicked point
    # From the reading in Advanced Methods in Computer Graphics by Ramakrishnan Mukundan,
    # Chapter 6.4 Inverse Kinematics
    #
    
    my = 480 - my;
    mx = mx - root_translate;
    temp = mx;
    mx = my;
    my = temp;

    
    #print str(pow((ROOT_LENGTH - seg_length), 2.0) <= pow(mx, 2.0) + pow(my, 2.0));
    #print str(pow(mx, 2.0) + pow(my, 2.0) <= pow((ROOT_LENGTH + seg_length), 2.0));
    if (((ROOT_LENGTH - seg_length) ** 2.0) <= (mx ** 2.0) + (my ** 2.0) and
        (mx ** 2.0) + (my ** 2.0) <= ((ROOT_LENGTH + seg_length) ** 2.0)) :
      
        cos2 = (acos(((mx ** 2.0) +
                      (my ** 2.0) -
                      (ROOT_LENGTH ** 2.0) -
                      (seg_length ** 2.0)) /
                     (2.0 * ROOT_LENGTH * seg_length)));
                    
        cos1 = (atan(my / mx) -
                atan(seg_length * sin(cos2) /
                     ((ROOT_LENGTH + seg_length * cos(cos2)))));
    else :
      return;

    if(my > 0):
      root_rotate = 90 - degrees(cos1);
      seg_rotate =  -degrees(cos2);
    else :
      root_rotate = degrees(cos1) ;
      seg_rotate = degrees(cos2) ;

    print str(root_rotate);
    print str(seg_rotate);



    # end TODO

# function for handling key down
def keyboard(c, x, y):
    global keys_down

    keys_down.add(c.lower())


# function for handling key up
def keyboardup(c, x, y):
    global keys_down

    keys_down.discard(c.lower())


# handle state update on timer
def timer(value):
    global keys_down
    global root_translate, root_rotate, seg_rotate, seg_length, finger_rotate

    dt = TIMER_TIME / 1000.0

    if 'q' in keys_down:
        root_rotate += ROTATE_SPEED * dt
    if 'w' in keys_down:
        root_rotate -= ROTATE_SPEED * dt

    if 'e' in keys_down:
        seg_rotate += ROTATE_SPEED * dt
    if 'r' in keys_down:
        seg_rotate -= ROTATE_SPEED * dt

    if 't' in keys_down:
        finger_rotate += ROTATE_SPEED * dt
    if 'y' in keys_down:
        finger_rotate -= ROTATE_SPEED * dt

    if 'a' in keys_down:
        root_translate -= TRANSLATE_SPEED * dt
    if 's' in keys_down:
        root_translate += TRANSLATE_SPEED * dt

    if 'd' in keys_down:
        seg_length -= TRANSLATE_SPEED * dt
    if 'f' in keys_down:
        seg_length += TRANSLATE_SPEED * dt


    glutPostRedisplay()
    glutTimerFunc(TIMER_TIME, timer, 0)


# function for displaying the game screen
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, SIZE, 0, SIZE);
 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(0.5, 0.5, 0.5)
    drawArm()
    
    glutSwapBuffers()


# startup
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(SIZE, SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboardup)
glutMouseFunc(mouseButton)
glutTimerFunc(TIMER_TIME, timer, 0)
glutMainLoop()
