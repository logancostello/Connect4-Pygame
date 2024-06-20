import pygame
import sys


def add_tuples(x, y):
    return tuple(map(lambda i, j: i + j, x, y))


def mult_tuples(x, y):
    return tuple(map(lambda i, j: i * j, x, y))


# initialize
pygame.init()

# setup
window_size = (800, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Connect 4")

# game board info
board_color = (55, 102, 163)
top_left = (50, 0)
board_rect = pygame.Rect(top_left, (700, 600))
piece_radius = 40
empty_color = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# setup game
def setup_game():
    screen.fill((255, 255, 255))  # Fill the screen with blue color

    # draw empty game
    pygame.draw.rect(screen, board_color, board_rect)

    # draw holes
    piece_offset = (50, 50)
    spacing = (100, 100)
    for i in range(7):
        for j in range(6):
            position = add_tuples(add_tuples(top_left, piece_offset),
                                  mult_tuples(spacing, (i, j)))
            pygame.draw.circle(screen, empty_color, position, piece_radius)

    # update
    pygame.display.flip()


# play game
setup_game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle window closing
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse")
            pygame.draw.circle(screen, red, pygame.mouse.get_pos(), piece_radius)

    # update
    pygame.display.flip()

# quit
pygame.quit()
sys.exit()
