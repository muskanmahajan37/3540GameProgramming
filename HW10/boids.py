import math, random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# constants
TIMER_TIME = 33
SIZE = 480
BOID_SPEED = 100
BOID_ACCEL = 10.0 # maximum accelleration of boid
WEIGHT_SEPARATION = 0.4
WEIGHT_ALIGNMENT = 0.1
WEIGHT_COHESION = 0.2
NBR_RADIUS = 80 # distance at which another boid is considered a neighbor
BOID_SIZE = 10


# state / constants
boids = [] # list of boids as [x position, y position, x velocity, y velocity] lists
boid_sel = None # index of selected boid, if any
use_separation = True
use_alignment = True
use_cohesion = True


def distance(b1, b2) :
        return math.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)


def get_neighbors_from_position(myBoid, ii):
    global boids, boid_sel
    nbr_ids = set()
    nbr_data = []

    for index in range(0, len(boids)) :
        if index == ii: continue
        potentialNeighbor = boids[index]
        if distance(myBoid, potentialNeighbor) < NBR_RADIUS :
            nbr_ids.add(index)
            nbr_data.append(potentialNeighbor)

    return nbr_ids, nbr_data



# return a list containing the indices, positions, and velocities of neighboring boids for the given boid index
def get_neighbors_for_boid(ii):
    global boids, boid_sel

    nbr_ids = set() # set of indices of neighbors
    nbr_data = [] # a list of 4-tuples (x, y, vx, vy) for position and velocity of neighbors

    # TODO: find neighbors (considering wrapping around edges)

    myBoid = boids[ii]

    # Check regular distance
    temp_ids, temp_data = get_neighbors_from_position(myBoid, ii)
    nbr_ids.update(temp_ids)
    nbr_data = nbr_data + temp_data

    if myBoid[0] < (0 + (NBR_RADIUS / 2)) :
        # If the x position is close to the left edge
        # simulate a boid at your position.x + size
        fakeBoid = [myBoid[0] + SIZE, myBoid[1]]
        temp_ids, temp_data = get_neighbors_from_position(fakeBoid, ii)
        nbr_ids.update(temp_ids)
        nbr_data = nbr_data + temp_data
    elif myBoid[0] > (SIZE - (NBR_RADIUS / 2)) :
        # If the x position is close to the right edge
        # simulate a boid at your position.x - SIZE
        fakeBoid = [myBoid[0] - SIZE, myBoid[1]]
        temp_ids, temp_data = get_neighbors_from_position(fakeBoid, ii)
        nbr_ids.update(temp_ids)
        nbr_data = nbr_data + temp_data

    if myBoid[1] < (0 + (NBR_RADIUS / 2)) :
        # If the y position is close to the bottom edges
        # simulate a boid at the positino.y + size
        fakeBoid = [myBoid[0], myBoid[1] + SIZE]
        temp_ids, temp_data = get_neighbors_from_position(fakeBoid, ii)
        nbr_ids.update(temp_ids)
        nbr_data = nbr_data + temp_data
    elif myBoid[1] > (SIZE - (NBR_RADIUS / 2)) :
        # IF the y pos is close to the top edge
        # simulate a boid at the position.y - SIZE
        fakeBoid = [myBoid[0], myBoid[1] - SIZE]
        temp_ids, temp_data = get_neighbors_from_position(fakeBoid, ii)
        nbr_ids.update(temp_ids)
        nbr_data = nbr_data + temp_data


    return nbr_ids, nbr_data


# get desired separation acceleration
def boid_separation_accel(boid, nbr_data):
    accel = [0.0, 0.0]

    # TODO: compute desired acceleration
    # Move in the oposite direction of the center of mass of neighbors

    veloSum = [0.0, 0.0]

    for nbr in nbr_data :
        veloSum[0] = veloSum[0] + (nbr[0] - boid[0])
        veloSum[1] = veloSum[1] + (nbr[1] - boid[1])

    veloSum[0] = veloSum[0] / (-1 * len(nbr_data))
    veloSum[1] = veloSum[1] / (-1 * len(nbr_data))

    #truncate(veloSum, 3.33)

    t = 7
    accel[0] = (veloSum[0] - boid[2]) / t
    accel[1] = (veloSum[1] - boid[3]) / t

    # multiply direction by some magnitude to generate the acceleration

    return accel



# get desired alignment acceleration
def boid_alignment_accel(boid, nbr_data):
    accel = [0.0, 0.0]

    # TODO: compute desired acceleration

    averageVelo = [0.0, 0.0]
    for nbr in nbr_data :
        averageVelo[0] = averageVelo[0] + nbr[2]
        averageVelo[1] = averageVelo[1] + nbr[3]
    averageVelo[0] = averageVelo[0] / len(nbr_data)
    averageVelo[1] = averageVelo[1] / len(nbr_data)


    #truncate(averageVelo, 3.33)

    t = 7
    accel[0] = (averageVelo[0] - boid[2]) / t
    accel[1] = (averageVelo[1] - boid[3]) / t

    return accel



# get desired cohesion acceleration
def boid_cohesion_accel(boid, nbr_data):
    accel = [0.0, 0.0]

    # TODO: compute desired acceleration
    # Move in the direction of the center of mass of neighbors

    centerOfMass = [0.0, 0.0]

    for nbr in nbr_data :
        centerOfMass[0] = centerOfMass[0] + nbr[0]
        centerOfMass[1] = centerOfMass[1] + nbr[1]
    centerOfMass[0] = centerOfMass[0] / len(nbr_data)
    centerOfMass[1] = centerOfMass[1] / len(nbr_data)

    # make a vector from the center of mass to us,
    direction = [centerOfMass[0] - boid[0], centerOfMass[1] - boid[1]]

    #truncate(direction, 3.33)

    t = 7
    accel[0] = (direction[0] - boid[2]) / t
    accel[1] = (direction[1] - boid[3]) / t

    return accel



# truncate vector to given magnitude and return magnitude
def truncate(vec, ml):
    ll = (vec[0] ** 2 + vec[1] ** 2) ** 0.5
    if ll > ml:
        vec[0] *= ml / ll
        vec[1] *= ml / ll
        return ml
    else:
        return ll


# steer a boid based on desired accelerations
def steer_boid(ii, nbr_data, dt):
    global boids, boid_se
    global use_separation, use_alignment, use_cohesion

    if len(nbr_data) != 0:
        separation_accel = [0, 0]
        if use_separation:
            separation_accel = boid_separation_accel(boids[ii], nbr_data)

        alignment_accel = [0, 0]
        if use_alignment:
            alignment_accel = boid_alignment_accel(boids[ii], nbr_data)

        cohesion_accel = [0, 0]
        if use_cohesion:
            cohesion_accel = boid_cohesion_accel(boids[ii], nbr_data)

        dvx, dvy = 0.0, 0.0
        accel_left = BOID_ACCEL
        for scale, accel in [(WEIGHT_SEPARATION, separation_accel), (WEIGHT_ALIGNMENT, alignment_accel), (WEIGHT_COHESION, cohesion_accel)]:
            accel[0] *= scale
            accel[1] *= scale
            ll = truncate(accel, accel_left)
            dvx += accel[0]
            dvy += accel[1]
            accel_left -= ll
            if accel_left <= 0.0:
                break

        boids[ii][2] += dvx
        boids[ii][3] += dvy

        spd = (boids[ii][2] ** 2 + boids[ii][3] ** 2) ** 0.5
        if spd > BOID_SPEED:
            boids[ii][2] *= BOID_SPEED / spd
            boids[ii][3] *= BOID_SPEED / spd
        elif spd < 0.7 * BOID_SPEED:
            boids[ii][2] *= 0.7 * BOID_SPEED / spd
            boids[ii][3] *= 0.7 * BOID_SPEED / spd


# function for drawing a single boid
def drawBoid():
    glBegin(GL_POLYGON)
    glVertex2f( 1.0,  0.0)
    glVertex2f(-0.5,  0.5)
    glVertex2f(-0.5, -0.5)
    glEnd()


# function for drawing all boids
def drawBoids():
    global boids, boid_sel

    nbr_ids, nbr_data = set(), []
    if boid_sel != None:
        nbr_ids, nbr_data = get_neighbors_for_boid(boid_sel)

    for ii, (px, py, vx, vy) in enumerate(boids):
        if ii == boid_sel:
            glColor3f(0.0, 1.0, 1.0)
        elif ii in nbr_ids:
            glColor3f(0.0, 0.2, 0.8)
        else:
            glColor3f(0.5, 0.5, 0.5)

        for dx, dy in [(0, 0), (SIZE, 0), (-SIZE, 0), (0, SIZE), (0, -SIZE)]:
            glPushMatrix()
            glTranslatef(px + dx, py + dy, 0)
            glRotatef(180.0 / math.pi * math.atan2(vy, vx), 0, 0, 1)
            glScalef(BOID_SIZE, BOID_SIZE, 1)
            drawBoid()
            glPopMatrix()


# mouse button handler
def mouseButton(button, state, mx, my):
    global boids, boid_sel

    if button != GLUT_LEFT_BUTTON:
        return

    if state != GLUT_DOWN:
        return

    wx = mx
    wy = SIZE - my - 1

    if glutGetModifiers() & GLUT_ACTIVE_SHIFT:
        sel_dist_sq = (2 * BOID_SIZE) ** 2
        boid_sel = None
        closest_sq = 1e100
        for ii, (px, py, vx, vy) in enumerate(boids):
            dist_sq = ((wx - px) ** 2 + (wy - py) ** 2)
            if dist_sq < sel_dist_sq and dist_sq < closest_sq:
                boid_sel = ii
                closest_sq = dist_sq
    else:
        angle = random.random() * math.pi * 2.0
        boids.append([wx, wy, BOID_SPEED * math.cos(angle), BOID_SPEED * math.sin(angle)])

    glutPostRedisplay()


# function for handling key down
def keyboard(c, x, y):
    global boids, boid_sel
    global use_separation, use_alignment, use_cohesion

    if c == ' ':
        boids = []
        boid_sel = None

    elif c == '1':
        use_separation = not use_separation

    elif c == '2':
        use_alignment = not use_alignment

    elif c == '3':
        use_cohesion = not use_cohesion

    glutPostRedisplay()


# handle state update on timer
def timer(value):
    global boids, boid_sel

    dt = TIMER_TIME / 1000.0

    for ii in xrange(len(boids)):
        nbr_ids, nbr_data = get_neighbors_for_boid(ii)
        steer_boid(ii, nbr_data, dt)

    for boid in boids:
        boid[0] += dt * boid[2]
        boid[1] += dt * boid[3]
        while boid[0] < 0.0:
            boid[0] += SIZE
        while boid[0] >= SIZE:
            boid[0] -= SIZE
        while boid[1] < 0.0:
            boid[1] += SIZE
        while boid[1] >= SIZE:
            boid[1] -= SIZE

    glutPostRedisplay()
    glutTimerFunc(TIMER_TIME, timer, 0)


# function to draw a string
def drawstring(x, y, j, s):
    CHAR_SIZE = 104.76
    NEW_SIZE = 10.0
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    if j > 0:
        glTranslatef(-NEW_SIZE * len(s), 0.0, 0.0)
    elif j == 0:
        glTranslatef(-0.5 * NEW_SIZE * len(s), 0.0, 0.0)
    glScalef(1.0/CHAR_SIZE, 1.0/CHAR_SIZE, 1.0)
    glScalef(NEW_SIZE, NEW_SIZE, 1.0)
    for c in s:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(c))
    glPopMatrix()


# function for displaying the game screen
def display():
    global boids, boid_se
    global use_separation, use_alignment, use_cohesion

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, SIZE, 0, SIZE);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    drawBoids()

    glColor3f(0.3, 0.3, 0.3)

    if use_separation:
        drawstring(10, 10, -1, 'separation')
    if use_alignment:
        drawstring(SIZE / 2.0, 10, 0, 'alignment')
    if use_cohesion:
        drawstring(SIZE - 10, 10, 1, 'cohesion')

    glutSwapBuffers()


# startup
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(SIZE, SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseButton)
glutTimerFunc(TIMER_TIME, timer, 0)
glutMainLoop()
