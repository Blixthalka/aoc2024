def read_file():
    f = open("input.txt", "r")
    left = []
    right = []

    for line in f:
        l = line.split()
        left.append(int(l[0]))
        right.append(int(l[1]))

    return (left, right)

def run_1():
    (left, right) = read_file()

    left_sorted = sorted(left)
    right_sorted = sorted(right)

    sum = 0
    for i in range(len(left)):
        left_min = left_sorted[i]
        right_min = right_sorted[i]
        sum += abs(left_min - right_min)

    print(sum)

def run_2():
    (left, right) = read_file()

    sum = 0
    for i in range(len(left)):
        left_num = left[i]
        sum += left_num * len(list(filter(lambda x: x == left_num, right)))

    print(sum)

run_1()
run_2()
