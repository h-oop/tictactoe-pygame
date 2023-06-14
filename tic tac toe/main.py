# tic tac toe?

import pygame

# init screen stuff
WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
CELL_SIZE = 200
GRID_SIZE = 3

# init colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

current_p = 'x'

grid = [
    (None, None, None), 
    (None, None, None), 
    (None, None, None)
    ]

def drawwindow():
    WIN.fill(BLACK)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell_x = event.pos[0] // CELL_SIZE
                cell_y = event.pos[1] // CELL_SIZE
                
                if grid[cell_y][cell_x] == None:
                    grid[cell_y][cell_x] = current_p
                    # change player
                    if current_p == 'x':
                        current_p = 'o'
                    else:
                        current_p = 'x'

        drawwindow()

    pygame.display.update()


main()