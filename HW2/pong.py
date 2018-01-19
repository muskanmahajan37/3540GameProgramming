import random, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# constants
TIMER_TIME = 33
INSET = 0.1
PADDLE_SPEED = 0.3
BALL_SPEED = 0.4
PADDLE_1_POSITION_X = 0.05
PADDLE_2_POSITION_X = 0.95
PADDLE_SIZE = 0.1
BALL_SIZE = 0.02

# Student added constants
CEILING = 0.84
FLOOR = 0.16

# keep track of which keys are down
keys_down = set()

# game state
paddle_1_score = 0
paddle_2_score = 0
paddle_1_position_y = 0.5
paddle_2_position_y = 0.5
ball_position_x = 0.5
ball_position_y = 0.5
ball_direction_x = None # note: if None, ball needs to be reset
ball_direction_y = None

# Student added game vars
game_started = 0

# function to draw a rectangle
def drawrect(cx, cy, w2, h2):
    glBegin(GL_QUADS)
    glVertex2f(cx - w2, cy - h2)
    glVertex2f(cx + w2, cy - h2)
    glVertex2f(cx + w2, cy + h2)
    glVertex2f(cx - w2, cy + h2)
    glEnd()


# function to draw a string
def drawstring(x, y, left, s):
    CHAR_SIZE = 104.76
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    if left:
        glTranslatef(-len(s) / 20.0, 0.0, 0.0)
    glScalef(1.0/CHAR_SIZE, 1.0/CHAR_SIZE, 1.0)
    glScalef(1.0/20.0, 1.0/20.0, 1.0)
    for c in s:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(c))
    glPopMatrix()


# normalize ball direction
def normalize_ball_direction():
    global ball_position_x, ball_position_y, ball_direction_x, ball_direction_y
    l = (ball_direction_x ** 2 + ball_direction_y ** 2) ** 0.5
    if l < 0.001:
        ball_position_x = None
    else:
        ball_direction_x /= l
        ball_direction_y /= l


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
    global paddle_1_position_y, paddle_2_position_y
    global ball_position_x, ball_position_y, ball_direction_x, ball_direction_y
    global paddle_1_score, paddle_2_score

    dt = TIMER_TIME / 1000.0

    # TODO: update game state
    
    # Move the paddles up and down
    if 'i' in keys_down:
      #paddle_2_position_y = paddle_2_position_y + (PADDLE_SPEED * 0.05)
      paddle_2_position_y = move_paddle_up(paddle_2_position_y)
    elif 'k' in keys_down:
      #paddle_2_position_y = paddle_2_position_y - (PADDLE_SPEED * 0.05)
      paddle_2_position_y = move_paddle_down(paddle_2_position_y)
    
    if 'w' in keys_down:
      paddle_1_position_y = move_paddle_up(paddle_1_position_y)
    elif 's' in keys_down:
      paddle_1_position_y = move_paddle_down(paddle_1_position_y)

    # move the ball
    move_ball()
    
    # end TODO

    glutPostRedisplay()
    glutTimerFunc(TIMER_TIME, timer, 0)


# checks and moves the ball
def move_ball() :
    global game_started
    global ball_direction_x
    global ball_direction_y
    global ball_position_x
    global ball_position_y
    
    
    if ball_direction_x == None or ball_direction_y == None:
      if len(keys_down) > 0 :
        # we're pressing a key start moving the ball
        ball_direction_x = 1
        ball_direction_y = 1
        normalize_ball_direction()
        
        x = random.randint(1,4)
        if x == 1 :
          # 1'st quadrent movement
          ball_direction_x *= 1
          ball_direction_y *= 1
        elif x == 2 :
          # 2nd quadrent movement
          ball_direction_x *= -1
          ball_direction_y *= 1
          
        elif x == 3:
          # 3rd quadrent movement
          ball_direction_x *= -1
          ball_direction_y *= -1
          
        elif x == 4 :
          # 4th quadrent movement
          ball_direction_x *= 1
          ball_direction_y *= -1

      else :
        # the game hasn't started yet don't move the ball
        return
    
    # check if the ball hit the ceiling or floor
    ball_size_skew = 0.05
    if ball_position_y > (CEILING + ball_size_skew) or ball_position_y < (FLOOR - ball_size_skew) :
      ball_direction_y *= -1

    # this will check for points, or paddle hits and update the ball direction or game state accordingly
    ball_hits_paddle_check()

    # now actually move the ball
    if ball_direction_y != None :
      ball_position_y += ball_direction_y * BALL_SPEED * 0.03
      ball_position_x += ball_direction_x * BALL_SPEED * 0.03

# check if a ball hit a paddle, or a back wall
# If a paddle is hit, update the direction of the ball
# If a wall is hit, update the score and restart the game
def ball_hits_paddle_check() :
    global ball_direction_x
    global ball_direction_y

    if ball_direction_x < 0 :
      # if the ball is moving to the left
      # consider paddle_1
      if ball_position_x < PADDLE_1_POSITION_X + (BALL_SIZE / 2) :
        # if the ball has hit the left edge of the 'game'
      
        # check to see if it is caught by a paddle
        if (ball_position_y < (paddle_1_position_y + (PADDLE_SIZE / 2)) and
            ball_position_y > (paddle_1_position_y - (PADDLE_SIZE / 2))) :
            # in a paddle
            ball_direction_x *= -1
        else :
          # not caught by a paddle, point to team 2
            update_score(2)
            reset_ball()
      # else the ball hasn't made it across the stage yet
    elif ball_direction_x > 0 :
      # if the ball is moving right
      # consider paddle_2
      if ball_position_x > PADDLE_2_POSITION_X - (BALL_SIZE / 2) :
        # if the ball has hit the right edge of the 'game'
      
        if (ball_position_y < (paddle_2_position_y + (PADDLE_SIZE / 2)) and
            ball_position_y > (paddle_2_position_y - (PADDLE_SIZE / 2))) :
            # in a paddle
            ball_direction_x *= -1
        else :
          # not caught by a paddle, point to team 1
          update_score(1)
          reset_ball()
      #else the ball hasn't made it across the stage yet

# updates the score depending on who got a point
def update_score(team) :
    global paddle_1_score
    global paddle_2_score
    
    if (team == 1) :
      paddle_1_score += 1
    elif (team == 2) :
      paddle_2_score += 1

# move the ball back to the center and reset direction to none
def reset_ball() :
    global ball_position_x
    global ball_position_y
    global ball_direction_x
    global ball_direction_y

    ball_position_x = 0.5
    ball_position_y = 0.5
    ball_direction_x = None
    ball_direction_y = None

# checks and moves the paddle up
def move_paddle_up(p_pos):
    if p_pos < CEILING:
      return p_pos + (PADDLE_SPEED * 0.05)
    else :
      return p_pos

# checks and moves the paddle down
def move_paddle_down(p_pos):
    if p_pos > FLOOR:
      return p_pos - (PADDLE_SPEED * 0.05)
    else :
      return p_pos

# function for displaying the game screen
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 1.0, 0.0, 1.0);
 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(1, 1, 1)

    drawrect(PADDLE_1_POSITION_X, paddle_1_position_y, BALL_SIZE/2, PADDLE_SIZE/2)
    drawrect(PADDLE_2_POSITION_X, paddle_2_position_y, BALL_SIZE/2, PADDLE_SIZE/2)
    drawrect(ball_position_x, ball_position_y, BALL_SIZE/2, BALL_SIZE/2)

    glBegin(GL_LINES)
    glVertex2f(0.0, INSET)
    glVertex2f(1.0, INSET)
    glVertex2f(0.0, 1.0 - INSET)
    glVertex2f(1.0, 1.0 - INSET)
    glEnd()

    drawstring(0.025, 0.925, False, str(paddle_1_score))
    drawstring(0.975, 0.925, True, str(paddle_2_score))

    glutSwapBuffers()


# startup
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 640)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboardup)
glutTimerFunc(TIMER_TIME, timer, 0)
glutMainLoop()
