import pygame
from ball import Ball
import numpy as np
import matplotlib.pyplot as plt

# Setup
pygame.init()
window_size = (1280,720)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
running = True
start_coordinates = (0, 0)
dt = 0.002
# Initialize first ball
player_pos = (screen.get_width()*0.25, screen.get_height()*0.65)
player = Ball(player_pos, 1, 10)
player.set_colour("dark green")
player.set_acceleration((0, 98.1))
player.set_elasticity(0.2)

# Testing data:
# player.set_initial_velocity((50, -100))
# player.moving = True

# Initialize map
floor = pygame.Rect(0, screen.get_height()*0.85, screen.get_width(), 100)
floor_color = "purple"
background_color = "grey"

def draw_map():
    # Initialize screen
    screen.fill(background_color)
    # Draw map objects
    pygame.draw.rect(screen, floor_color, floor)

def draw_player():
    pygame.draw.circle(screen, player.get_colour(), player.get_position(), player.get_radius())


while running:

    # Check for events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw map
    draw_map()
    # Draw player
    draw_player()

    # Render game
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    
    dragging = True
    if pygame.mouse.get_pressed()[0]:
        start_coordinates = pygame.mouse.get_pos()

        while dragging:
            # draw_map()

            event = pygame.event.wait()

            if event.type == 1026:
                stop_coordinates = pygame.mouse.get_pos()
                dragging = False
            elif event.type == 1024:
                draw_map()
                draw_player()
                pygame.draw.line(screen, "red", start_coordinates, pygame.mouse.get_pos(), 2)

            # Render game0
            pygame.display.flip()
        
        player.set_initial_velocity(
            (start_coordinates[0]-stop_coordinates[0], start_coordinates[1]-stop_coordinates[1])
        )
        player.moving = True
        
    
    pygame.time.wait(100)
    clock.tick(60) 

    if np.abs(player.get_velocity()[0]) > 0 or np.abs(player.get_velocity()[1]) > 0:

        while player.moving:
            
            # Check if the player will collide in the next position (with floor)
            collision = player.check_collision(
                (floor.left, floor.right, floor.bottom, floor.top), dt
            )
            
            if player.collision:
                player.resolve_collision(floor.top)

            player.set_position(
                player.calculate_next_position(dt)
            )

            player.calculate_velocity(dt)

            # Redraw content
            draw_map()
            draw_player()

            # Render game
            pygame.display.flip()
            dt = clock.tick(60) / 600
pygame.quit()