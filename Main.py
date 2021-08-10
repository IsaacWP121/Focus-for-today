import pygame, sys, random
import button
pygame.init()
size = width, height = 550, 400
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Focus for today")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
areas = ["Movement", "Projectiles", "Punish Game", "Combos", "DI", "Save burst", "Git Gud"]
b = button.Button(screen, 2, 8, (0, 0, 0))

while 1:
    screen.fill(WHITE)
    b.update_size()
    b.addText()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if b.x+b.bw>pos[0]>b.x and b.y+b.bh>pos[1]>b.y:
                if b.Words in areas:
                    b.Words = "Focus for today"
                else:
                    def rand():
                        return random.choice(areas)
                    x = rand()
                    if x == "Git Gud":
                        x = rand()
                    b.Words= x
        if event.type == pygame.VIDEORESIZE:
            b.update_size()
            if b.font_size < 10 or event.h <= 150:
                pygame.display.set_mode((width, height),pygame.RESIZABLE)
            else:
                width = event.w
                height = event.h     
    pygame.display.update()
    clock.tick(30)