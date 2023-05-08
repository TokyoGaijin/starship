import pygame
import Character
import ship
import colorswatch as cs

screen_size = (640, 480)
surface = pygame.display.set_mode(screen_size)
bgcol = cs.black["pygame"]
bgimage = pygame.image.load("gameboard.png")
clock = pygame.time.Clock()
FPS = 60

captain = Character.Officer("human", "captain", "Kirk", "command", gender="male", surface=surface)
enterprise = ship.Ship(surface, 0, 0)

isDemoOn = True


while isDemoOn:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDemoOn = False

    # captain.avatarVisible = True
    surface.blit(bgimage, (0, 0))
    captain.draw()
    captain.update()
    enterprise.draw_alert()
    enterprise.update()


    pygame.display.update()
    surface.fill(bgcol)

