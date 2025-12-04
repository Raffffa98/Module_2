import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() 
running = True

x = screen.get_width() / 2
y = screen.get_height() / 2

delta_Time = 0

circle_position = pygame.Vector2(x, y)

while running:

    for event in pygame.event.get(): #pygame.event.get() is for getting events (inputs) from queue
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            running = False

        screen.fill("black")

    pygame.draw.circle(screen, "purple", circle_position, 100)

    Keys = pygame.key.get_pressed()

    if Keys [pygame.k.w]:
        circle_position.y -= 300 * delta_Time



    pygame.display.flip()

    delta_Time = clock.tick(60) / 1000

pygame.quit()

    