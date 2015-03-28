import sys
import pygame
import Scenebase
import Dataloader


class AvatarScene(Scenebase.SceneBase):

    def __init__(self):
       self.next = self

    def ProcessInput(self, events, keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.SwitchToScene(ActionsScene())

    def Update(self):
        pass

    def Render(self, screen):
        fontH1 = pygame.font.SysFont(self.font_family, 40, bold=False, italic=False)
        header = fontH1.render("Welcome to United People", True, (255,0,0), self.colorBG)
        headerPos = header.get_rect()
        headerPos.centerx = screen.get_rect().centerx
        #headerPos.centery = screen.get_rect().centery
        headerPos.centery = 45
        
        screen.fill(self.colorBG)
        screen.blit(header, headerPos)

        #pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))
        avWidth = 200
        avHeight = 350
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(screen.get_rect().centerx - avWidth/2,
                                                          screen.get_rect().centery - avHeight/2,
                                                          avWidth,
                                                          avHeight))

class ActionsScene(Scenebase.SceneBase):
    
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        fontH1 = pygame.font.SysFont(self.font_family, 40, bold=False, italic=False)
        header = fontH1.render("Your Self", True, (255,0,0), self.colorBG)
        headerPos = header.get_rect()
        headerPos.centerx = screen.get_rect().centerx
        #headerPos.centery = screen.get_rect().centery
        headerPos.centery = 45

        screen.fill(self.colorBG)
        screen.blit(header, headerPos)

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
