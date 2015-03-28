import pygame
import Globals


class Menu(object):
    
    bgColor = (200, 200, 200)
    fgColor = (255, 0, 0)
    hlColor = (20, 20, 20)
    font = pygame.font.SysFont(Globals.font_family, 18, bold=False, italic=False)
    top = 0
    left = 0
    
    """A Menu"""
    
    def __init__(self, itemList):
        super(Menu, self).__init__()
        self.itemList = itemList
        
    def setColors(self, bgColor, fgColor, hlColor):
        self.bgColor = bgColor
        self.fgColor = fgColor
        self.hlColor = hlColor
        
    def draw(self):
        for item in self.itemList:
            print(item)