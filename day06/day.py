
def read_file():
    f = open("input.txt", "r")
    grid = []

    for l in f:
        grid.append(list(l.strip()))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return (grid, y, x)


NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

def run_1():
    (grid, start_y, start_x) = read_file()
    (_, visited) = traverse(grid, start_y, start_x)
    print(len(visited))


def run_2():
    (grid, start_y, start_x) = read_file()

    (_, visited) = traverse(grid, start_y, start_x)
    visited = list(map(lambda item: item[0], visited))

    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#' or (y == start_y and x == start_x) or (not (y, x) in visited):
                continue

            grid[y][x] = '#'
            (has_loop, _) = traverse(grid, start_y, start_x)
            if has_loop:
                sum += 1

            grid[y][x] = '.'

    print(sum)


def traverse(grid, start_y, start_x):
    dir = NORTH
    visited = {
        ((start_y, start_x), dir)
    }
    y = start_y
    x = start_x

    while True:
        (dy, dx) = dir
        y_new = y + dy
        x_new = x + dx

        if (y_new < 0 or y_new >= len(grid)):
            break
        if (x_new < 0 or x_new >= len(grid[y_new])):
            break

        if grid[y_new][x_new] == '#':
            if dir == NORTH:
                dir = EAST
            elif dir == EAST:
                dir = SOUTH
            elif dir == SOUTH:
                dir = WEST
            elif dir == WEST:
                dir = NORTH
            continue

        y = y_new
        x = x_new
        visited_item = ((y, x), dir)
        if visited_item in visited:
            return (True, visited)

        visited.add(visited_item)

    return (False, visited)

run_1()
run_2()
