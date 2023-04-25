import pygame

pygame.init()

running = True

screen = pygame.display.setmode((300, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ())
    pygame.display.flip()
