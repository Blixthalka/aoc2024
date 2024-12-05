import re

def read_file():
    f = open("input.txt", "r")
    ll = []
    for line in f:
        ll.append(line.strip())
    return ll

def run_1():
    input = read_file()
    sum = 0

    for y in range(len(input)):
        for x in range(len(input[y])):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dx == 0 and dy == 0):
                        continue
                    sum += search_xmas(input, x, y, dx, dy)

    print(sum)


def search_xmas(input, x, y, dx, dy):
    search = "XMAS"
    for i in range(4):
        x_new = x + i * dx
        y_new = y + i * dy

        if (y_new < 0 or y_new >= len(input)):
            return 0
        if (x_new < 0 or x_new >= len(input[y_new])):
            return 0

        if input[y_new][x_new] != search[i]:
            return 0

    return 1


def run_2():
    input = read_file()
    sum = 0

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 'A':
                TopLeft = get_letter(input, y - 1, x - 1)
                BottomRight = get_letter(input, y + 1, x + 1)
                TopRight = get_letter(input, y - 1, x + 1)
                BottomLeft = get_letter(input, y + 1, x - 1)

                if TopLeft is None or BottomLeft is None or BottomRight is None or TopRight is None:
                    continue

                if TopLeft != BottomRight and TopRight != BottomLeft:
                    sum += 1

    print(sum)


def get_letter(input, y, x):
    if (y < 0 or y >= len(input)):
        return None
    if (x < 0 or x >= len(input[y])):
        return None

    if (input[y][x] == 'S' or input[y][x] == 'M'):
        return input[y][x]

    return None



run_1()
run_2()
