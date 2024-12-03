import re

def read_file():
    f = open("input.txt", "r")
    ll = ""
    for line in f:
        ll += line
    return ll

def run_1():
    input = read_file()
    sum = 0
    for (x, y) in re.findall("mul\((\d+),(\d+)\)", input):
         sum += int(x) * int(y)
    print(sum)


def run_2():
    input = read_file()
    instructions = [(m.start(0), m.group(1), m.group(2)) for m in re.finditer("mul\((\d+),(\d+)\)", input)]
    dos = [(m.start(0), m.group(0)) for m in re.finditer("don?'?t?\(\)", input)]

    sum = 0
    for (index, x, y) in instructions:
        match = find(index, dos)
        if match != "don't()":
            sum += int(x) * int(y)
    print(sum)

def find(index, list):
    prev = None
    for item in list:
        (i, value) = item
        if i > index:
            return prev
        prev = value
    return None


run_1()
run_2()
