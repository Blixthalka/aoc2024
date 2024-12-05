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
    sum = 0
    enabled = True
    for match in re.finditer("(don?'?t?\(\))|mul\((\d+),(\d+)\)", input):
        if (match.group(0) == "don't()"):
            enabled = False
        elif (match.group(0) == "do()"):
            enabled = True
        elif enabled:
            sum += int(match.group(2)) * int(match.group(3))

    print(sum)


run_1()
run_2()
