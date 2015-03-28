import sys
import pygame
import Scenebase


class AvatarScene(Scenebase.SceneBase):

    def __init__(self):
       self.next = self

    def ProcessInput(self, events, keys):
        # for event in events:
        #     if event.type == sys.QUIT:
        #         pygame.quit()
        #         sys.exit()
        pass

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        font_family = "Century Gothic"
        fontH1 = pygame.font.SysFont(font_family, 40, bold=False, italic=False)
        header = fontH1.render("Welcome to United People", True, (255,0,0), self.colorBG)
        headerPos = header.get_rect()
        headerPos.centerx = screen.get_rect().centerx
        #headerPos.centery = screen.get_rect().centery
        headerPos.centery = 45
        
        screen.fill(self.colorBG)
        screen.blit(header, headerPos)
