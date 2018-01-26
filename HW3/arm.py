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
    
    # Move root into position
    glTranslatef(root_translate, ROOT_LENGTH/2, 0);
    #rotate the toot
    glTranslatef(ROOT_WIDTH/2, -ROOT_LENGTH/2, 0);
    glRotatef(root_rotate, 0, 0, -1);
    glTranslatef(-ROOT_WIDTH/2, ROOT_LENGTH/2, 0);
    
    glPushMatrix()
    glScalef(ROOT_WIDTH, ROOT_LENGTH, 1);

    drawSquare(); # draw the root
    glPopMatrix();

    # Move seg into position (relative to arm)
    glTranslatef(SEG_WIDTH/8, (ROOT_LENGTH/2) + (seg_length/2) , 0);
    # rotate the seg
    glTranslatef(SEG_WIDTH/2 , -seg_length/2, 0);
    glRotatef(seg_rotate, 0, 0, 1);
    glTranslatef(-SEG_WIDTH/2 , seg_length/2, 0);
    
    
    glPushMatrix();
    glScalef(SEG_WIDTH, seg_length, 1);
    drawSquare();  # draw the seg
    glPopMatrix();
    
    glPushMatrix();  # save state, so we can return for the other fingers
    
    # Building first finger on the left
    glTranslatef(0, (seg_length/2) + (FINGER_LENGTH/2), 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);
    
    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare(); # firsts finger on the left
    glPopMatrix();
    
    # Building second finger on the left
    glTranslatef(0, FINGER_LENGTH, 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(-finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);
    
    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare(); # second finger on the left
    glPopMatrix();
    
    glPopMatrix(); # finsihed left fingers

    # Building first finger on the right
    glTranslatef(SEG_WIDTH - FINGER_WIDTH, (seg_length/2) + (FINGER_LENGTH/2), 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(-finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);

    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();  # First finger on the right
    glPopMatrix();

    # Building second finger on the firhgt
    glTranslatef(0, FINGER_LENGTH, 0);
    glTranslatef(FINGER_WIDTH/2, -FINGER_LENGTH/2, 0);
    glRotatef(finger_rotate, 0, 0, 1);
    glTranslatef(-FINGER_WIDTH/2, FINGER_LENGTH/2, 0);

    glPushMatrix();
    glScalef(FINGER_WIDTH, FINGER_LENGTH, 1);
    drawSquare();  # Second finger on the right
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
    
    my = SIZE - my;
    mx = mx - root_translate;
    temp = mx;
    mx = my;
    my = temp;


    if (((ROOT_LENGTH - seg_length) ** 2.0) <= (mx ** 2.0) + (my ** 2.0) and
        (mx ** 2.0) + (my ** 2.0) <= ((ROOT_LENGTH + seg_length) ** 2.0)) :
      
        ang2 = (acos(((mx ** 2.0) +
                      (my ** 2.0) -
                      (ROOT_LENGTH ** 2.0) -
                      (seg_length ** 2.0)) /
                     (2.0 * ROOT_LENGTH * seg_length)));
                    
        ang1 = (atan(my / mx) -
                atan(seg_length * sin(ang2) /
                     ((ROOT_LENGTH + seg_length * cos(ang2)))));

    else :
      return;


    # Unfortunatly I couldn't figure out how to get the elbow to 'bend' in the
    # other direction.
    root_rotate = degrees(ang1);
    seg_rotate =  -degrees(ang2);



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
