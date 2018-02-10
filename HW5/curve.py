import random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

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


def dist(p0, p1) :
  return math.sqrt((math.pow((p0[0] - p1[0]), 2)) + (math.pow((p0[1] - p1[1]), 2)))

def scalePoint(s, p) :
  return ( p[0] * s, p[1] * s)

def addPoints(p1, p2) :
  return (p1[0] + p2[0], p1[1] + p2[1])

def drawBezier(p0, p1, p2, p3):
  global FLATNESS_EPSILON
  # if the points are straight enough then draw them, otherwise split into 2 curves
  # and recurse

  # If len(p0 -> p1) + len(p1 -> p2) + len(p2 -> p3)
  #    ---------------------------------------------      <  1 + FLATNESS_EPSILON
  #                 len(p0 -> p3)
  # else:
  #     recur


  totalEdgeLen = dist(p0, p1) + dist(p1, p2) + dist(p2, p3)
  directEdgeLen = dist(p0, p3)
  if (totalEdgeLen / directEdgeLen) < (1 + FLATNESS_EPSILON) :
    # base case, draw a single line connecting p0 -> p3
    glVertex2f(p0[0], p0[1])
    glVertex2f(p3[0], p3[1])

  else :
    
    # else, split the curve in half and recur
    t = 0.5
    
    p11 = addPoints(scalePoint(1.0 - t, p0) , scalePoint(t, p1))
    p21 = addPoints(scalePoint(1.0 - t, p2) , scalePoint(t, p3))
    p = addPoints(scalePoint(1.0 - t, p11) , scalePoint(t, p21))
    
    # Draw the left side:
    drawBezier(p0, p11,  p11, p)

    # Draw the right side
    drawBezier(p, p21, p21, p3)




# function for drawing a curve
def drawCurve():
    global ctype, handles

    if ctype == TYPE_BEZIER:
        # TODO: draw Bezier curve from handles
        
        handleCount = 0
        while (handleCount + 4) <= len(handles) :
          # while there are at least 4 more handles
          drawBezier(handles[handleCount + 0],
                     handles[handleCount + 1],
                     handles[handleCount + 2],
                     handles[handleCount + 3])
        
          handleCount += 3
        
        
        # End TODO
        pass

    else:
        # TODO: draw Catmull-Rom curve from handles
        
        if len(handles) >= 4 :
        
          # For every 4-tuple of handles
          for i in range(0, len(handles) - 3) :
            p0 = handles[i + 0]
            p1 = handles[i + 1]
            p2 = handles[i + 2]
            p3 = handles[i + 3]
            
            lineSegments = 20
            curvePointsLen = 0
            curvePoints = []
            percentTwenty = 1.0 / float(lineSegments)
            for j in range(0, lineSegments) :  # 20 line segements requires 21 points
              t = percentTwenty * float(j)
              # Generate the point at time t
              tm = np.matrix( ((1.0, t, (math.pow(t, 2)), (math.pow(t, 3)) )) )
              m  = np.matrix( ((0.0, 1.0, 0.0, 0.0), (-0.5, 0.0, 0.5, 0.0), (1.0, -2.5, 2.0, -0.5), (-0.5, 1.5, -1.5, 0.5)) )
              pm = np.matrix( ((p0), (p1), (p2), (p3)) )

              temp1 = np.dot(m, pm)
              temp2 = np.dot(tm, temp1)  ## calculated end/start point for the next line segment

              curvePoints.append(temp2)
              curvePointsLen += 1
              #print "    adding to curvePoints: " + str(temp2)
            # end generating curve points
            
            
            for pi in range(0, curvePointsLen - 1) :
              glVertex2f(curvePoints[pi].item(0),     curvePoints[pi].item(1))
              glVertex2f(curvePoints[pi + 1].item(0), curvePoints[pi + 1].item(1))
            # end drawing curve lines
            
          # end looping throuhg handles
          
        # End TODO
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
