import random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import heapq
from sets import Set
from time import sleep

# constants
CELL_SIZE = 10
SIZE = 40

# view state
cells = None # grid of cells of the world
start = None # starting position
searched = set() # set of cells searched for path
path = None # list of cells along path from start to goal


def manhatanDist(current, target):
    return abs(current[0] - target[0]) + abs(current[1] - target[1])

# run astar
def astar(goal):
    global cells, start

    # TODO: implement astar, return a list of the cells from the start to goal
    # (or None if there is no path) and a set of the cells searched


    #print(cells)
    #print(cells[0])

    frontier = []
    temp = manhatanDist(start, goal)
    heapq.heappush(frontier, (temp, start))
    cameFrom =  {}
    cameFrom[start] = None
    costSoFar = {}
    costSoFar[start] = 0

    searched = set()

    while len(frontier) > 0 :
        current = heapq.heappop(frontier)[1]
        if (current[0] == goal[0]) and (current[1] == goal[1]) :
            break

        # Add all of current's neighbors to the frontier

        # For every neighbor
        for xx in range(-1, 2) :
            for yy in range(-1, 2):
                neighborX = current[0] + xx
                neighborY = current[1] + yy

                # Error checking for walls and bounds
                if neighborX < 0 or neighborX >= SIZE :
                    continue
                if neighborY < 0 or neighborY >= SIZE :
                    continue
                if (cells[neighborX][neighborY] == 1) :
                    # If there is a wall, ignore it
                    continue


                neighborPos = neighborX, neighborY
                tempCost = costSoFar[current] + 1
                if not(neighborPos in costSoFar) or (tempCost < costSoFar[neighborPos]) :
                    costSoFar[neighborPos] = tempCost
                    priority = tempCost + manhatanDist(neighborPos, goal)

                    cameFrom[neighborPos] = current
                    heapq.heappush(frontier, (priority, neighborPos))
                    searched.add(neighborPos)




    path = []
    current = goal
    print
    while not((current[0] == start[0]) and (current[1] == start[1])) :
        # While we are not currently on the start
        print("current: " + str(current))
        path.append(cameFrom[current])
        current = cameFrom[current]

    path.append(start)

    return path, searched


# create a new world
def newWorld():
    global cells, start, searched, path

    cells = [[0 for i in xrange(SIZE)] for i in xrange(SIZE)]
    for ii in xrange(30):
        ll = random.randint(3, 10)
        xx = random.randint(0, SIZE - 1 - ll)
        yy = random.randint(0, SIZE - 1 - ll)
        if random.randint(0, 1) == 0:
            dx = 1
            dy = 0
        else:
            dx = 0
            dy = 1

        for jj in xrange(ll):
            if xx >= SIZE or yy >= SIZE:
                break

            cells[xx][yy] = 1
            xx += dx
            yy += dy

    while True:
        start = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))
        if cells[start[0]][start[1]] == 0:
            break

    searched = set()
    path = None


# mouse button handler
def mouseButton(button, state, xx, yy):
    global cells, start, searched, path

    if button != GLUT_LEFT_BUTTON:
        return

    if state != GLUT_DOWN:
        return

    pt = (xx / CELL_SIZE, (SIZE * CELL_SIZE - yy - 1) / CELL_SIZE)

    path, searched = astar(pt)

    glutPostRedisplay()


# function for handling key down
def keyboard(c, x, y):
    if c == ' ':
        newWorld()

        glutPostRedisplay()


# function for displaying a cell
def displayCell(xx, yy):
    glVertex2f((xx + 0) * CELL_SIZE, (yy + 0) * CELL_SIZE)
    glVertex2f((xx + 1) * CELL_SIZE, (yy + 0) * CELL_SIZE)
    glVertex2f((xx + 1) * CELL_SIZE, (yy + 1) * CELL_SIZE)
    glVertex2f((xx + 0) * CELL_SIZE, (yy + 1) * CELL_SIZE)


# function for displaying the game screen
def display():
    global cells, start, searched, path

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, CELL_SIZE * SIZE, 0, CELL_SIZE * SIZE);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glBegin(GL_QUADS)
    for xx in xrange(SIZE):
        for yy in xrange(SIZE):
            if (xx, yy) == start:
                glColor3f(0.8, 0.0, 0.8)
            elif path != None and (xx, yy) in path:
                if cells[xx][yy] == 1:
                    glColor3f(1.0, 0.0, 0.0)
                else:
                    idx = path.index((xx, yy))
                    glColor3f(0.0, 0.2 + 0.8 * (idx / float(len(path) - 1)), 0.0)
            elif searched != None and (xx, yy) in searched:
                if cells[xx][yy] == 1:
                    glColor3f(1.0, 0.0, 0.0)
                else:
                    glColor3f(0.0, 0.1, 0.3)
            elif cells[xx][yy] == 1:
                glColor3f(0.5, 0.5, 0.5)
            else:
                glColor3f(0.0, 0.0, 0.0)

            displayCell(xx, yy)
    glEnd()

    glutSwapBuffers()


# startup
random.seed(12345)
newWorld()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(CELL_SIZE * SIZE, CELL_SIZE * SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseButton)
glutMainLoop()
