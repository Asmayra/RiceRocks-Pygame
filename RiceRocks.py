"""
 RiceRocks implementation in Pygame

"""

import pygame
import os

# import PNG
nebula_image = pygame.image.load(os.path.join("img/nebula_blue.f2014.png"))
debris_image = pygame.image.load(os.path.join("img/debris2_blue.png"))
debris_image = pygame.transform.scale(debris_image, (800,600))
splash_image = pygame.image.load(os.path.join("img/splash.png"))

# globals
WIDTH = 800
HEIGHT = 600
time = 0
score = 0
lives = 3
started = False







pygame.init()
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rice Rocks")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here





    # draw Background
    time += 1
    wtime = (time / 4) % WIDTH
    screen.blit(nebula_image, (0,0))
    screen.blit(debris_image, (wtime , 0))
    screen.blit(debris_image, (wtime - WIDTH , 0))

    # draw UI


    if not started:
        screen.blit(splash_image, (WIDTH / 4, HEIGHT / 4))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
