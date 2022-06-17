from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # création fenetre
pygame.display.set_caption("Drawing Program")


def init_grid(rows, cols, color):  # création grid
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                             PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))  # on place les pixels

    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, i*PIXEL_SIZE),
                             (WIDTH, i*PIXEL_SIZE))
        for i in range(COLS+1):
            pygame.draw.line(win, BLACK, (i*PIXEL_SIZE, 0),
                             (i*PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid):  # mise en place du BG
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    pygame.display.update()


run = True
clock = pygame.time.Clock()  # initialisation des fps
grid = init_grid(ROWS, COLS, BG_COLOR)

while run:  # boucle du jeu

    clock.tick(FPS)

    for event in pygame.event.get():  # jeu s'arrête si on appuie sur la croix ^^
        if event.type == pygame.QUIT:
            run = False

    draw(WIN, grid)


pygame.quit
