from hashlib import blake2b
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


def draw(win, grid, buttons):  # mise en place du BG et des boutons
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)
    pygame.display.update()


# connaitre la postion du pixel qui doit changer de couleur
def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    return row, col


run = True
clock = pygame.time.Clock()  # initialisation des fps
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(310, button_y, 50, 50, WHITE, "Clear", BLACK),


]

while run:  # boucle du jeu

    clock.tick(FPS)

    for event in pygame.event.get():  # jeu s'arrête si on appuie sur la croix ^^
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()  # permet de connaitre la position de la souris
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:  # on regarde si on a cliqué sur un bouton
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

    draw(WIN, grid, buttons)


pygame.quit
