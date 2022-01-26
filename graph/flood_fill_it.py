def isOutOfBounds(screen, x, y):
    N = len(screen)
    M = len(screen[0])

    x_out_of_bounds = x < 0 or x >= N
    y_out_of_bounds = y < 0 or y >= M

    return x_out_of_bounds or y_out_of_bounds


def should_recolor(screen, x, y, new_color, initial_color):
    return (
        not isOutOfBounds(screen, x, y)
        and screen[x][y] == initial_color
        and screen[x][y] != new_color
    )


def should_enqueue(screen, x, y, new_color, initial_color, visited):
    return should_recolor(screen, x, y, new_color, initial_color) and not visited[x][y]


def floodFill(screen, x, y, new_color):
    initial_color = screen[x][y]

    if initial_color == new_color:
        return

    N = len(screen)
    M = len(screen[0])

    # Visited matrix for BFS (cycles may happen)
    visited = [[False] * M for _ in range(N)]

    queue = [(x, y)]
    while queue:
        x, y = queue.pop(-1)

        screen[x][y] = new_color

        if should_enqueue(screen, x + 1, y, new_color, initial_color, visited):
            visited[x + 1][y] = True
            queue.append((x + 1, y))

        if should_enqueue(screen, x - 1, y, new_color, initial_color, visited):
            visited[x - 1][y] = True
            queue.append((x - 1, y))

        if should_enqueue(screen, x, y + 1, new_color, initial_color, visited):
            visited[x][y + 1] = True
            queue.append((x, y + 1))

        if should_enqueue(screen, x, y - 1, new_color, initial_color, visited):
            visited[x][y - 1] = True
            queue.append((x, y - 1))


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
