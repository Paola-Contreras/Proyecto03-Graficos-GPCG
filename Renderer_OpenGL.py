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

# Model No. 1 Plant 
rend.target.z -= 5

plant = Model("indoor plant_02.obj", "indoor plant_2_COL.bmp")

plant.position.z -= 5
plant.position.y = -1.3

plant.scale.x = 0.4
plant.scale.y = 0.4
plant.scale.z = 0.4

# Model No. 2 Sofa 
Sofa = Model("Couch.obj", "Couch_Base_Color.bmp")

Sofa.position.z -= 5
Sofa.position.y = -1

Sofa.scale.x = 1.5
Sofa.scale.y = 1.5
Sofa.scale.z = 1.5


# Model No. 3 Sofa 
face = Model("Yoshi.obj", "Yoshi.bmp")

face.position.z -= 5
face.position.y = -1

face.scale.x = 1.5
face.scale.y = 1.5
face.scale.z = 1.5

rend.scene.append( Sofa )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        # --------------- SHADERS ----------------------
            elif event.key == pygame.K_1:
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_2:
                rend.setShaders(vertex_shader, toon_shader)
            elif event.key == pygame.K_3:
                rend.setShaders(fat_shader, fragment_shader)
            elif event.key == pygame.K_4:
                rend.setShaders(vertex_shader, rainbow_shader)
            elif event.key == pygame.K_5:
                rend.setShaders(sphere_shader, fragment_shader)
            elif event.key == pygame.K_6:
                rend.setShaders(vertex_shader, OnOff_shader)
            #elif event.key == pygame.K_7:
            #    rend.wireframeMode()

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

    # --------------- TIME ----------------------
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    # -------------------------------------------
    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
