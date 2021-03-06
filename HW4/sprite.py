import random, sys, time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# constants
TIMER_TIME = 33
SIZE = 480

TIMERS_PER_SPRITE = 8 # how many timer events should be called before moving to the next frame in sprite animation

SHEET_DATA = None # sprite sheet data, filled in later
SHEET_SIZE_I = 126, 144 # size of entire sprite sheet, in pixels

SPRITE_SIZE_I = 34, 36 # actual size of each sprite, in pixels
SPRITE_STRIDE_I = 46, 36 # how much space each sprite takes up in the sheet, in pixels

SPRITE_SIZE = SPRITE_SIZE_I[0] / float(SHEET_SIZE_I[0]), SPRITE_SIZE_I[1] / float(SHEET_SIZE_I[1]) # sprite size realtive to sheet size
SPRITE_STRIDE = SPRITE_STRIDE_I[0] / float(SHEET_SIZE_I[0]), SPRITE_STRIDE_I[1] / float(SHEET_SIZE_I[1]) # sprite space relative to sheet size


# state
keys_down = set()

sprite_index = [1, 3] # which sprite to displat
cycle_index = 0 # which frame (0 - 3) in the animation to display
last_sprite_change = TIMERS_PER_SPRITE # how many more timer calls until the animation moves forward a frame
texture = None # texture ID


# function to determine texture coordinates
def gettexcoords():
    global sprite_index

    coords = [
        0., # lower u/x texture coord
        0., # lower v/y texture coord
        1., # upper u/x texture coord
        1.  # upper v/y texture coord
        ]

    # TODO: compute texture coordinates based on sprite_index
    
    # lets say we want, (1, 3)
    #  We need to move over 2 sprite strides
    #                  up 4 sprite strides
    
    # Our bottom left point will be:
    pixelDeltaBLX = sprite_index[0] * SPRITE_STRIDE_I[0]
    pixelDeltaBLY = sprite_index[1] * SPRITE_STRIDE_I[1]
    
    # Our top right point will be our bottom right + sprite actual size
    pixelDeltaTRX = pixelDeltaBLX + SPRITE_SIZE_I[0]
    pixelDeltaTRY = pixelDeltaBLY + SPRITE_SIZE_I[1]

    # Convert delta into %
    coords = [
        pixelDeltaBLX / float(SHEET_SIZE_I[0]),
        pixelDeltaBLY / float(SHEET_SIZE_I[1]),
        pixelDeltaTRX / float(SHEET_SIZE_I[0]),
        pixelDeltaTRY / float(SHEET_SIZE_I[1])
        ]
    
        
    # End TODO

    return coords


# function to load in texture from file
def loadtexture():
    global SHEET_DATA

    import base64, pickle, zlib
    imdata = pickle.loads(zlib.decompress(base64.b64decode(SHEET_DATA)))

    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, SHEET_SIZE_I[0], SHEET_SIZE_I[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, imdata)

    return tex
    

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
    global sprite_index, last_sprite_change, cycle_index

    dt = TIMER_TIME / 1000.0

    # TODO: update sprite state based on keys down
    
    # Direction specifies the Sprite-Index-Y value
    si_y = sprite_index[1]
    if "w" in keys_down :     # Looking up
      si_y = 1
    elif "a" in keys_down :    # Looking Left
      si_y = 0
    elif "s" in keys_down :    # Looking Down
      si_y = 3
    elif "d" in keys_down :    # Looking Right
      si_y = 2

    # Update cycle_index/ last_sprite_change
    if last_sprite_change >= TIMERS_PER_SPRITE:
      cycle_index = (cycle_index + 1) % 4
      last_sprite_change = 0
    else :
      last_sprite_change += 1

    # Frame/cycle specifies the Sprite-Index-X value
    si_x = 1
    if cycle_index == 0 :
      si_x = 0
    elif cycle_index == 2:
      si_x = 2

    sprite_index = [si_x, si_y]
    #print "last_sprite_change " + str(last_sprite_change)
    
    #end TODO

    glutPostRedisplay()
    glutTimerFunc(TIMER_TIME, timer, 0)


# function for displaying the game screen
def display():
    global texture

    if texture == None:
        texture = loadtexture()

    glClearColor(0, 0.2, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, 1, 0, 1);
 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(1, 1, 1)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)

    coords = gettexcoords()

    glPushMatrix()
    glTranslate(0.5 - SPRITE_SIZE[0] / 2., 0.5 - SPRITE_SIZE[1] / 2., 0.)

    glBegin(GL_QUADS)
    glTexCoord2f(coords[0], coords[1])
    glVertex2f(0.0, 0.0)
    glTexCoord2f(coords[2], coords[1])
    glVertex2f(SPRITE_SIZE[0], 0.0)
    glTexCoord2f(coords[2], coords[3])
    glVertex2f(SPRITE_SIZE[0], SPRITE_SIZE[1])
    glTexCoord2f(coords[0], coords[3])
    glVertex2f(0.0, SPRITE_SIZE[1])
    glEnd()

    glPopMatrix()

    glutSwapBuffers()


# sprite sheet data (modified from Curt - cjc83486 - https://opengameart.org/content/rpg-character)
SHEET_DATA = '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'


# startup
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(SIZE, SIZE)
glutCreateWindow('CS3540')
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboardup)
glutTimerFunc(TIMER_TIME, timer, 0)
glutMainLoop()
