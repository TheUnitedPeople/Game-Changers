import Scenes

__author__ = 'Iago Mosquera'

import sys
import pygame
import yaml

from pygame.locals import *

DWIDTH = 1280
DHEIGHT = 720

#pygame.init()
#DISPLAYSURF = pygame.display.set_mode((DWIDTH, DHEIGHT))
#pygame.display.set_caption('United People')

#colorBG = (20, 20, 20)

# Utils

def loadfile(datafile):
    file = open(datafile, 'r')
    data = yaml.load(file)

# Pseudomodules

# def avatarScreen():
#     font_family = "Century Gothic"
#     fontH1 = pygame.font.SysFont(font_family, 40, bold=False, italic=False)
#     header = fontH1.render("Welcome to United People", True, (255,0,0), colorBG)
#     headerPos = header.get_rect()
#     headerPos.centerx = DISPLAYSURF.get_rect().centerx
#     #headerPos.centery = DISPLAYSURF.get_rect().centery
#     headerPos.centery = 45
    
#     DISPLAYSURF.fill(colorBG)
#     DISPLAYSURF.blit(header, headerPos)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        #active_scene.ProcessInput(pressed_keys)
        
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)

# Main loop

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
#     avatarScreen()

run_game(DWIDTH, DHEIGHT, 60, Scenes.AvatarScene())

