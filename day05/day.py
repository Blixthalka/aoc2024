import re

def read_file():
    f = open("input.txt", "r")
    ordering_rules = []
    updates = []

    ordering = True
    for l in f:
        line = l.strip()
        if line == "":
            ordering = False
            continue

        if ordering:
            ordering_rules.append([int(x) for x in line.split("|")])
        else:
            updates.append([int(x) for x in line.split(",")])


    ordering_map = {}
    for ordering_rule in ordering_rules:
        before = ordering_rule[0]
        after = ordering_rule[1]

        if before in ordering_map:
            ordering_map[before].append(after)
        else:
            ordering_map[before] = [after]

    return (ordering_map, updates)

def run_1():
    (ordering_map, updates) = read_file()
    sum = 0
    for update in updates:
        sum += update_score(update, ordering_map)
    print(sum)


def update_score(update, ordering_map):
    for i in range(len(update)):
        before = update[i]
        for j in range(i+1, len(update)):
            after = update[j]
            if after in ordering_map and before in ordering_map[after]:
                return 0
    return update[int(len(update)/2)]

def run_2():
    (ordering_map, updates) = read_file()
    sum = 0
    for update in updates:
        if update_score(update, ordering_map) == 0:
            sum += update_score(reorder(update, ordering_map), ordering_map)

    print(sum)

def reorder(update, ordering_map):
    for i in range(len(update)):
        before = update[i]
        for j in range(i+1, len(update)):
            after = update[j]
            if update[j] in ordering_map and before in ordering_map[update[j]]:
                update[i] = after
                update[j] = before
                return reorder(update, ordering_map)

    return update

run_1()
run_2()
