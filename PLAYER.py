import pygame
from CONSTANTS import *


class Player_1_2:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                                PADDLE_HEIGHT)
        self.SPEED = 20
        self.color = (0, 0, 0)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def move_up(self):
        self.rect.y -= self.SPEED
        self.keep_in_bounds()

    def move_down(self):
        self.rect.y += self.SPEED
        self.keep_in_bounds()


    def keep_in_bounds(self):
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - self.rect.height)
        self.rect.y = max(0, self.rect.y)


class Player_3_4:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_2_WIDTH // 2, SCREEN_HEIGHT - PADDLE_2_HEIGHT, PADDLE_2_WIDTH,
                                PADDLE_2_HEIGHT)
        self.SPEED = 20
        self.color = (0, 0, 0)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def move_left(self):
        self.rect.x -= self.SPEED
        self.keep_in_bounds()

    def move_right(self):
        self.rect.x += self.SPEED
        self.keep_in_bounds()

    def keep_in_bounds(self):
        self.rect.x = min(self.rect.x, SCREEN_WIDTH - self.rect.width)
        self.rect.x = max(0, self.rect.x)
