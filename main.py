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
player_pos = (screen.get_width()*0.25, screen.get_height()*0.75)
player = Ball(player_pos, 1, 10)
player.set_colour("red")
player.set_initial_velocity((50, -150))
player.set_acceleration((0, 98.1))

while running:

    # Check for events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initialize screen
    screen.fill("grey")



    # Draw player
    pygame.draw.circle(screen, player.get_colour(), player.get_position(), player.get_radius())


    # Initialize and draw map (floor) 
    floor = pygame.Rect(0, screen.get_height()*0.9, screen.get_width(), 20)
    pygame.draw.rect(screen, "purple", floor)

    # run limit:
    k = 1
    params = []

    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:

        player.moving = True
        while player.moving:
            
            # Check if the player will collide in the next position (with floor)
            collision = player.check_collision(
                (floor.left, floor.right, floor.bottom, floor.top), dt
            )
            
            print(player.get_position())
            print((floor.left, floor.right, floor.top, floor.bottom))
            print((floor.left <= player.get_position()[0] <= floor.right, '---' ,floor.top <= player.get_position()[1] <= floor.bottom))
            print(player.collision)
            
            if player.collision:
                player.resolve_collision(floor.top)
                print('COLLISION!')
                print(floor.bottom, floor.top, player.calculate_next_position(dt))
            print()
            player.set_position(
                player.calculate_next_position(dt)
            )

            player.calculate_velocity(dt)

            params.append([player.get_position(), player.get_velocity(), player.get_acceleration()])






            k += 1

            if k > 1:
                player.moving = False
        
            pygame.draw.circle(screen, player.get_colour(), player.get_position(), player.get_radius())
            pygame.time.wait(10)


    # Render game
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()