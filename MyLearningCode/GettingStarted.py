import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() 
running = True

x = screen.get_width() / 2
y = screen.get_height() / 2

circle_position = pygame.Vector2(x, y)

while running:

    for event in pygame.event.get(): #pygame.event.get() is for getting events (inputs) from queue
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:

    screen.fill("black")

    pygame.draw.circle(screen, "purple", circle_position, 100)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()

    