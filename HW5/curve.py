import random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# constants
SIZE = 480
HANDLE_SIZE = 9
FLATNESS_EPSILON = 0.00005

TYPE_BEZIER = 0
TYPE_CATMULLROM = 1

# view state
ctype = TYPE_BEZIER
handles = []
activeHandle = None
showHandles = True


# function for drawing a curve
def drawCurve():
    global ctype, handles

    if ctype == TYPE_BEZIER:
        # TODO: draw Bezier curve from handles
        pass

    else:
        # TODO: draw Catmull-Rom curve from handles
        pass


# mouse button handler
def mouseButton(button, state, mx, my):
    global handles, activeHandle

    if button != GLUT_LEFT_BUTTON:
        return

    if state == GLUT_DOWN:
        closest = 1e100
        for ii, (hx, hy) in enumerate(handles):
            if abs(hx - mx) <= HANDLE_SIZE / 2 and abs(hy - my) <= HANDLE_SIZE / 2:
                distsq = (hx - mx) ** 2 + (hy - my) ** 2
                if distsq < closest:
                    closest = distsq
                    activeHandle = ii

        if activeHandle == None:
            handles.append((mx, my))
            activeHandle = len(handles) - 1

    if state == GLUT_UP:
        activeHandle = None

    glutPostRedisplay()


# mouse motion handler
def mouseMotion(mx, my):
    global handles, activeHandle

    if activeHandle != None:
        handles[activeHandle] = (mx, my)

        glutPostRedisplay()


# function for handling key down
def keyboard(ch, mx, my):
    global ctype, handles, activeHandle, showHandles

    if ch == ' ':
        handles = []
        activeHandle = None

    elif ch.lower() == 't':
        if ctype == TYPE_BEZIER:
            ctype = TYPE_CATMULLROM
        else:
            ctype = TYPE_BEZIER

    elif ch.lower() == 's':
        showHandles = not showHandles

    glutPostRedisplay()


# function for displaying the game screen
def display():
    global handles, activeHandle, showHandles

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, SIZE, SIZE, 0);
 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    if showHandles:
        glColor3f(0.2, 0.2, 0.2)
        glBegin(GL_LINE_STRIP)
        for hx, hy in handles:
            glVertex2f(hx, hy)
        glEnd()

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_LINES)
    drawCurve()
    glEnd()

    if showHandles:
        glBegin(GL_QUADS)
        for ii, (hx, hy) in enumerate(handles):
            if activeHandle != None and activeHandle == ii:
                glColor3f(0.5, 0.5, 1.0)
            else:
                glColor3f(0.8, 0.8, 0.8)

            glVertex2f(hx - 0.5 * HANDLE_SIZE, hy - 0.5 * HANDLE_SIZE)
            glVertex2f(hx + 0.5 * HANDLE_SIZE, hy - 0.5 * HANDLE_SIZE)
            glVertex2f(hx + 0.5 * HANDLE_SIZE, hy + 0.5 * HANDLE_SIZE)
            glVertex2f(hx - 0.5 * HANDLE_SIZE, hy + 0.5 * HANDLE_SIZE)
        glEnd()

    glutSwapBuffers()


# startup
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(SIZE, SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseButton)
glutMotionFunc(mouseMotion)
glutPassiveMotionFunc(mouseMotion)
glutMainLoop()
