import pygame

__author__ = 'iacusm'


class SceneBase:

    font_family = "Century Gothic"

    colorBG = (20, 20, 20)

    def __init__(self):
        self.next = self

    def ProcessInput(self, events, keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
        