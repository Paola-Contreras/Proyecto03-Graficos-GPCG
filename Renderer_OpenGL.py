from pickle import TRUE
import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

 # --------------- MODEL ----------------------

rend.target.z -= 5

face = Model("indoor plant_02.obj", "indoor plant_2_COL.bmp")

face.position.z -= 5
face.position.y = -1.3

face.scale.x = 0.4
face.scale.y = 0.4
face.scale.z = 0.4


rend.scene.append( face )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()

    # --------------- CAMARA MOVEMENTS ----------------------

    mousepositions = pygame.mouse.get_rel()

    #Zoom In & Out
    if event.type == pygame.MOUSEWHEEL:
        if rend.camDistance >= 2 and rend.camDistance <= 10:
            rend.camDistance -= (event.y * 2) * deltaTime
        elif rend.camDistance < 2:
            rend.camDistance = 2 
        elif rend.camDistance > 10:
            rend.camDistance = 10

    #Left & Right
    rend.angle -= mousepositions[0]* deltaTime * 13

    #Up & Down
    if rend.camPosition.y >= -2 and rend.camPosition.y <= 2:
        rend.camPosition.y += mousepositions[1]* deltaTime
    elif rend.camPosition.y < -2:
        rend.camPosition.y = -2
    elif rend.camPosition.y > 2:
        rend.camPosition.y = 2





    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    

     # --------------- LIGHTS MOVEMENT ----------------------
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
