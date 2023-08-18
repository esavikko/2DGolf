import pygame
from ball import Ball

import matplotlib.pyplot as plt

# Setup
pygame.init()
window_size = (1280,720)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
running = True

# Initialize first ball
player_pos = (screen.get_width()*0.25, screen.get_height()*0.65)
player = Ball(player_pos, 1, 10)
player.set_colour("red")
player.set_initial_velocity((50, -150))
player.set_acceleration((0, 98.1))
player.set_elasticity(1)

# Initialize map
floor = pygame.Rect(0, screen.get_height()*0.75, screen.get_width(), 20)
floor_color = "purple"
background_color = "grey"


while running:

    # Check for events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initialize screen
    screen.fill(background_color)

    # Draw map objects
    pygame.draw.rect(screen, floor_color, floor)

    # Draw player
    pygame.draw.circle(screen, player.get_colour(), player.get_position(), player.get_radius())




    # Render game
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:

        player.moving = True
        while player.moving:
            
            # Check if the player will collide in the next position (with floor)
            collision = player.check_collision(
                (floor.left, floor.right, floor.bottom, floor.top), dt
            )
            
            # print(player.get_velocity())
            
            if player.collision:
                player.resolve_collision(floor.top)

            player.set_position(
                player.calculate_next_position(dt)
            )

            player.calculate_velocity(dt)

            # Redraw content
            screen.fill('grey')
            pygame.draw.rect(screen, "purple", floor)
            pygame.draw.circle(screen, player.get_colour(), player.get_position(), player.get_radius())
            

            # Render game
            pygame.display.flip()
            dt = clock.tick(60) / 600

pygame.quit()