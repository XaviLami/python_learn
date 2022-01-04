from Player import Perso
import pygame 

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Space Invader 3000")

loop = True
p = Perso()
while loop:
    ecran.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                p.dir = "up"
            if event.key == pygame.K_q:
                p.dir = "left" 
            if event.key == pygame.K_s:
                p.dir = "down"
            if event.key == pygame.K_d:
                p.dir = "right"
            if event.key == pygame.K_p:
                loop = False 
        if event.type == pygame.QUIT:
            loop = False
    p.Update()
    p.Draw(ecran)
    pygame.display.flip()
pygame.quit()