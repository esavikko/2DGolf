import pygame
import numpy as np

class Ball:

    def __init__(self, position, mass, radius) -> None:

        self.position = position            # tuple
        self.mass = mass                    # float
        self.radius = radius                # float
        self.colour = "white"               # str

        self.moving = False                 # boolean
        self.velocity = (0, 0)              # tuple
        self.acceleration = (0, 0)          # tuple
        self.collision = False              # boolean, check if bounce is required
        self.elasticity = 0.8
    
    def get_position(self) -> tuple:
        return self.position
    
    def set_position(self, next_position) -> None:

        if isinstance(next_position, tuple):
            self.check_if_moving()
            if self.moving:
                self.position = next_position

    def set_elasticity(self, elasticity) -> None:
        if isinstance(elasticity, float):
            if 0 < elasticity <= 1:
                self.elasticity = elasticity
    
    def check_if_moving(self) -> None:
        if (np.abs(self.velocity[0]) < 1) and (np.abs(self.velocity[1]) < 1):
                print('Player has stopped moving.')
                self.velocity = (0, 0)
                self.moving = False

    def get_velocity(self) -> tuple:
        return self.velocity
    
    def set_initial_velocity(self, initial_velocity) -> None:
        self.velocity = initial_velocity
    
    def calculate_velocity(self, t) -> None:

        self.velocity = (
            (self.velocity[0] + self.acceleration[0]*t), (self.velocity[1] + self.acceleration[1]*t)
        )

    def set_acceleration(self, acceleration) -> None:
        if isinstance(acceleration, tuple):
            self.acceleration = acceleration

    def get_acceleration(self) -> tuple:
        return self.acceleration
    
    def get_colour(self) -> str:
        return self.colour
    
    def set_colour(self, new_colour) -> None:
        if isinstance(new_colour, str):
            self.colour = new_colour

    def get_radius(self) -> float:
        return float(self.radius)
    
    def calculate_next_position(self, t) -> tuple:

        next_position = (self.position[0] + self.velocity[0] * t + 0.5 * self.acceleration[0] * (t**2),
                        self.position[1] + self.velocity[1] * t + 0.5 * self.acceleration[1] * (t**2))
        return next_position
    
    def check_collision(self, check_position, t):
        
        next_position = self.calculate_next_position(t)
        # check_position is defined as down_x, up_x, left_y, right_y
        if check_position[0] <= next_position[0] <= check_position[1]:
            if check_position[2] >= next_position[1] >= check_position[3]: # Y axis is reversed
                self.collision = True
    
    def resolve_collision(self, floor_x):

        dx = self.position[1] - floor_x

        self.position = (self.position[0], self.position[1] - dx)
        self.velocity = (self.elasticity * self.velocity[0], -self.elasticity * self.velocity[1])

        self.collision = False





