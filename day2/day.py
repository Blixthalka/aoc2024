import operator


def read_file():
    f = open("input.txt", "r")
    reports = []

    for line in f:
        reports.append(list(map(lambda x: int(x), line.split())))

    return reports

def run_1():
    reports = read_file()
    valid = len(list(filter(lambda r: validate(r), reports)))
    print(valid)

def run_2():
    reports = read_file()
    valid = len(list(filter(lambda r: validate_problem_dampener(r), reports)))
    print(valid)


def validate_problem_dampener(report):
    for i in range(len(report)):
        res = validate(report[:i] + report[i+1:])
        if (res):
            return True

    return False

def validate(report):
    return validate_op(operator.gt, report) or validate_op(operator.lt, report)

def validate_op(op, report):
    prev = None
    for level in report:
        if prev is None:
            prev = level
            continue

        if op(prev, level):
            return False

        diff = abs(prev - level)
        if diff > 3 or diff == 0:
            return False

        prev = level
    return True


run_1()
run_2()
