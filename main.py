# CENG487 Assignment1 by
# Goyaqua
# StudentId: 
# 03/2025

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import numpy as np
import time

from modules.Object3D import Object3D
from modules.Vec3D import Vec3D

window = 0

# Create a triangle and a square
def createTriangle():
    return Object3D([
        Vec3D(0, 1, 0, 1),
        Vec3D(-1, -1, 0, 1),
        Vec3D(1, -1, 0, 1)
    ])

def createSquare():
    return Object3D([
        Vec3D(-1, -1, 0, 1),
        Vec3D(1, -1, 0, 1),
        Vec3D(1, 1, 0, 1),
        Vec3D(-1, 1, 0, 1)
    ])

# Create objects
triangle = createTriangle()
square = createSquare()

# Initial translations
initial_translation_triangle = Vec3D(-1.5, 0, -6, 1)
initial_translation_square = Vec3D(1.5, 0, -6, 1)

# Frame rate
targetFrameRate = 30
timePerFrame = 1.0 / targetFrameRate
deltaTime = time.time()
increaseRotate = 0

# Initialize OpenGL
def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Resize OpenGL
def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Draw OpenGL Scene
def DrawGLScene():
    # Global variables
    global triangle, square, deltaTime, increaseRotate
    currentTime = time.time() # Get current time
    elapsedTime = currentTime - deltaTime # Calculate elapsed time

    if elapsedTime >= timePerFrame: # If elapsed time is greater than time per frame
        deltaTime = currentTime # Update delta time
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear buffers
        drawObject(triangle, GL_TRIANGLES, initial_translation_triangle, 1, colored=True)
        drawObject(square, GL_QUADS, initial_translation_square, 1, colored=False)
        glutSwapBuffers() # Swap buffers

# Draw object with given drawType, initialTranslationVec, rotationSpeed and colored
def drawObject(obj, drawType, initialTranslationVec, rotationSpeed, colored=True):
    global increaseRotate
    glLoadIdentity()

    # find center of object
    center = Vec3D(0, 0, 0, 0)
    for v in obj.vertices:
        center += v
    center /= len(obj.vertices)

    obj.clear_transformations()

    # to rotate around its center
    # translate to origin, rotate, translate back to pivot
    obj.translate(-center.x, -center.y, -center.z) 
    obj.rotate_y(np.radians(increaseRotate)) 
    obj.translate(center.x, center.y, center.z) 
    obj.translate(initialTranslationVec.x, initialTranslationVec.y, initialTranslationVec.z)

    # draw object
    transformed = obj.transformed_vertices()
    obj.clear_transformations()

    glBegin(drawType)
    for i, v in enumerate(transformed):
        if colored:
            if i == 0:
                glColor3f(1, 0, 0)
            elif i == 1:
                glColor3f(0, 1, 0)
            else:
                glColor3f(0, 0, 1)
        else:
            glColor3f(0.3, 0.5, 1.0)
        glVertex3f(v.x, v.y, v.z)
    glEnd()

    increaseRotate += rotationSpeed

# Handle key press
# Hit ESC to quit
def keyPressed(key, x, y):
    if ord(key) == 27:
        glutLeaveMainLoop()
        return

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"CENG487 Object3D Transform Test")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()

print("Hit ESC to quit.")
main()
