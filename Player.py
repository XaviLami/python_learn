import pygame
class Perso:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.taille = 1
        self.tab= None
        self.vit = 1
        self.dir ="none"

    def Draw(self, ecran):
        pygame.draw.circle(ecran, (  0,   0, 255), (self.x,self.y), 20)

    def Update(self):
        if self.dir == "up":
            self.y-=self.vit
        elif self.dir == "down":
            self.y+=self.vit
        elif self.dir == "left":
            self.x-=self.vit
        elif self.dir == "right":
            self.x+=self.vit
        