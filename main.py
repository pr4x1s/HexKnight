import pygame
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("idk the name yet")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#  okay so this is game for resume I guess
#  The idea is like a board game on a hexagonal grid
#  To-do list:
#  Draw the grid :-)

while True:
    window.fill(WHITE)
    pygame.draw.polygon(window, BLACK, ((0,0), (10, 10), (20, 200)), width=3)
    pygame.display.flip()