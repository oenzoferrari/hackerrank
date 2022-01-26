def isOutOfBounds(screen, x, y):
    N = len(screen)
    M = len(screen[0])

    x_out_of_bounds = x < 0 or x >= N
    y_out_of_bounds = y < 0 or y >= M

    return x_out_of_bounds or y_out_of_bounds


def floodFillHelper(screen, x, y, previous_color, new_color):
    if (
        isOutOfBounds(screen, x, y)
        or screen[x][y] != previous_color
        or screen[x][y] == new_color
    ):
        return

    screen[x][y] = new_color

    floodFillHelper(screen, x + 1, y, previous_color, new_color)
    floodFillHelper(screen, x - 1, y, previous_color, new_color)
    floodFillHelper(screen, x, y + 1, previous_color, new_color)
    floodFillHelper(screen, x, y - 1, previous_color, new_color)


def floodFill(screen, x, y, new_color):
    initial_color = screen[x][y]

    if initial_color == new_color:
        return

    floodFillHelper(screen, x, y, initial_color, new_color)


screen = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

M = len(screen)
N = len(screen[0])

x = 4
y = 4
new_color = 3

floodFill(screen, x, y, new_color)


for i in range(M):
    for j in range(N):
        print(screen[i][j], end=" ")
    print()
