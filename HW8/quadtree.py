import random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# constants
WORLD_SIZE = 480
OBJECT_SIZE = 20 # size of each object
MAX_TREE_DEPTH = 4 # max depth to subdivide quadtree to

# view state
objects = [] # all objects in world
objects_selected = None # list of object selected after click
quadtree = None # the quadtree


# class representing a quadtree node
class Node:
    # initialize node
    def __init__(self, bounds, depth):
        self._bounds = bounds # bounds of this node as ((x0, y0), (x1, y1))
        self._depth = depth # depth of this node
        self._objects = [] # objects in this node
        self._children = None # child nodes: None or four
        self._visited = False # use this to determine if a node was visited during traversal

    # clear all visited flags
    def clearVisited(self):
        self._visited = False
        if self._children:
            for child in self._children:
                child.clearVisited()

    # do some basic checks of the tree structure
    def checkStructure(self):
        if self._objects and self._children:
            raise RuntimeError("Node has objects and children.")
        if self._depth > MAX_TREE_DEPTH:
            raise RuntimeError("Node depth greater than max depth.")

        if self._children:
            for child in self._children:
                child.checkStructure()

    # recursively display a node
    def display(self, showVisited):
        (x0, y0), (x1, y1) = self._bounds

        if showVisited:
            if self._visited:
                glColor(0.0, 0.0, float(self._depth + 1) / (MAX_TREE_DEPTH + 2))
                glBegin(GL_QUADS)
                glVertex2f(x0, y0)
                glVertex2f(x1, y0)
                glVertex2f(x1, y1)
                glVertex2f(x0, y1)
                glEnd()
        else:
            if self._objects != None and len(self._objects) != 0:
                glColor(0.2, 0.2, 0.2)
                glBegin(GL_QUADS)
                glVertex2f(x0, y0)
                glVertex2f(x1, y0)
                glVertex2f(x1, y1)
                glVertex2f(x0, y1)
                glEnd()

        glColor(0.5, 0.5, 0.5)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x0, y0)
        glVertex2f(x1, y0)
        glVertex2f(x1, y1)
        glVertex2f(x0, y1)
        glEnd()

        if self._children:
            for child in self._children:
                child.display(showVisited)

    # insert an object into the quadtree, changing the tree structure as needed
    def insertObject(self, object):

        if (len(self._objects) == 0) and (not self._children) :
            # If there are no objects in this node
            # AND there are no children nodes
            self._objects.append(object)
            return

        # Else, there either already are other objects, or there are children

        # Check to see if we need to make new children, and sort existing
        # object
        if (len(self._objects) != 0) :
            # If there are _objects

            if (self._depth < MAX_TREE_DEPTH) :
                # If we are allowed to subdivide more
                # Make 4 nodes
                (x0, y0), (x1, y1) = self._bounds
                w = (x1 - x0) / 2
                h = (y1 - y0) / 2
                q1 = Node(((x0 + w, y0 + h), (x1,     y1)),     self._depth + 1)
                q2 = Node(((x0,     y0 + h), (x0 + w, y1)),     self._depth + 1)
                q3 = Node(((x0,     y0),     (x0 + w, y0 + h)), self._depth + 1)
                q4 = Node(((x0 + w, y0),     (x1,     y0 + h)), self._depth + 1)

                #print("Building children: ")
                #print ("(x0: " + str(x0) + ") (y0: " + str(y0) + ") (x1: " + str(x1) + ") (y1: " + str(y1))
                #print ("W: " + str(w) + "     h: " + str(h))
                #print ("q1: " + str(((x0 + w, y0 + h), (x1,     y1))))
                #print ("q2: " + str(((x0,     y0 + h), (x0 + w, y1))))
                #print ("q3: " + str(((x0,     y0),     (x0 + w, y0 + h))))
                #print ("q4: " + str(((x0 + w, y0),     (x1,     y0 + h))))

                self._children = [q1, q2, q3, q4]

                # move all objects in here to the correct child
                # there should only be 1 _objects at a time
                xx, yy = self._objects[0]
                sl = OBJECT_SIZE / 2
                # 1 asume it is entierly contained within this node
                # (and newly made children)
                if ((xx - sl) < (x0 + w)) :
                    # If the obj is on the left hand part of the nodes
                    if ((yy - sl) < (y0 + h)) :
                        # obj is left and down => q3
                        q3.insertObject(self._objects[0])
                    if ((yy + sl) >= (y0 + h)) :
                        # obj is left and up => q2
                        q2.insertObject(self._objects[0])
                if ((xx + sl) >= (x0 + w)) :
                    # obj is right
                    if ((yy - sl) < (y0 + h)) :
                        # obj is right and down => q4
                        q4.insertObject(self._objects[0])
                    if ((yy + sl) >= (y0 + h)) :
                        # obj is right and up => q1
                        q1.insertObject(self._objects[0])

                self._objects = []

            else :
                # else we are not allowed to subdivide,
                self._objects.append(object)

        # Below will sort new incoming object into correct child
        if (self._children) :
            # Figure out which child to put the new obj into
            xx, yy = object
            (x0, y0), (x1, y1) = self._bounds
            w = (x1 - x0) / 2
            h = (y1 - y0) / 2
            sl = OBJECT_SIZE / 2

            # Assume the cube is entierly contained within this node
            if ((xx - sl) < (x0 + w)) :
                # Left most of obj is on left half
                if ((yy - sl) < (y0 + h)) :
                    # obj is left and down => q3
                    self._children[2].insertObject(object)
                if ((yy + sl) >= (y0 + h)) :
                    # obj is left and up => q2
                    self._children[1].insertObject(object)
            if ((xx + sl) >= (x0 + w)) :
                # obj is right
                if ((yy - sl) < (y0 + h)) :
                    # obj is right and down => q4
                    self._children[3].insertObject(object)
                if ((yy + sl) >= (y0 + h)) :
                    # obj is right and up => q1
                    self._children[0].insertObject(object)

            # Now check
        pass

    # find any objects in the tree that contain the given point
    def findObjects(self, pt):
        # TODO: traverse tree to see if any objects were selected, return empty list if not found

        self._visited = True

        x, y = pt
        (x0, y0), (x1, y1) = self._bounds
        w = (x1 - x0) / 2
        h = (y1 - y0) / 2
        sl = OBJECT_SIZE / 2

        if (len(self._objects) != 0 ) :
            result = []
            # If there are objects in this block
            # Check to see if we clicked on any
            print("Found objects. count: " + str(len(self._objects)))
            print("Obj xy: " + str(self._objects[0]))
            for i in range(0, len(self._objects)) :
                curObj = self._objects[i]
                objX, objY = curObj
                # Check each object to see if the pt is inside it
                xRange = ((objX - sl) <= x) and (x <= (objX + sl))
                yRange = ((objY - sl) <= y) and (y <= (objY + sl))

                if xRange and yRange :
                    print("Clicked on object!")
                    result.append(curObj)
                    print(result)
            print("returning result: " + str(result))
            return result


        if (self._children) :
            # If there are children
            # Recur down and simulate a click on the correct children

            if (x < x0 + w ) :
                # If we click left
                if (y < y0 + h) :
                    # If we click left AND down => q3
                    return self._children[2].findObjects(pt)
                else :
                    # If we click left AND up => q2
                    return self._children[1].findObjects(pt)
            else :
                # Else we clicked right
                if (y < y0 + h) :
                    # If we click right AND down => q4
                    return self._children[3].findObjects(pt)
                else :
                    # If we click right AND up => q1
                    return self._children[0].findObjects(pt)

        # Else there are no children, and no objects
        return []
        pass


# generate new world
def newWorld():
    global objects, objects_selected, quadtree

    objects = []
    objects_selected = None
    quadtree = Node(((0, 0), (WORLD_SIZE, WORLD_SIZE)), 0)

    n = random.randint(5, 15)

    for i in xrange(n):
        x = random.randint(OBJECT_SIZE, WORLD_SIZE - OBJECT_SIZE - 1)
        y = random.randint(OBJECT_SIZE, WORLD_SIZE - OBJECT_SIZE - 1)
        object = (x, y)
        objects.append(object)
        quadtree.insertObject(object)

    quadtree.checkStructure()


# mouse button handler
def mouseButton(button, state, xx, yy):
    global objects, objects_selected, quadtree

    if button != GLUT_LEFT_BUTTON:
        return

    if state != GLUT_DOWN:
        return

    quadtree.clearVisited()
    objects_selected = quadtree.findObjects((xx, WORLD_SIZE - yy - 1))
    print("result in mouseButton: " + str(quadtree.findObjects((xx, WORLD_SIZE - yy - 1))))
    print("objects_selected: " + str(objects_selected))

    glutPostRedisplay()


# function for handling key down
def keyboard(c, x, y):
    if c == ' ':
        newWorld()
        glutPostRedisplay()


# function for displaying the game screen
def display():
    global objects, objects_selected, quadtree

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, WORLD_SIZE, 0, WORLD_SIZE)

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    quadtree.display(objects_selected != None)

    glBegin(GL_QUADS)
    for obj in objects:
        if objects_selected and obj in objects_selected:
            glColor3f(1, 1, 0)
        else:
            glColor3f(1, 1, 1)
        xx, yy = obj
        glVertex2f(xx - OBJECT_SIZE / 2, yy - OBJECT_SIZE / 2)
        glVertex2f(xx + OBJECT_SIZE / 2, yy - OBJECT_SIZE / 2)
        glVertex2f(xx + OBJECT_SIZE / 2, yy + OBJECT_SIZE / 2)
        glVertex2f(xx - OBJECT_SIZE / 2, yy + OBJECT_SIZE / 2)
    glEnd()

    glutSwapBuffers()


# startup
random.seed(12345)
newWorld()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(WORLD_SIZE, WORLD_SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseButton)
glutMainLoop()
