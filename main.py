import itertools

import numpy as np
from progressbar import *
from scipy.spatial import distance

length = 4
max_num = 10


def columns(table):
    r = []
    for y in range(length):
        sum = sum(table[x][y] for x in range(length))
        r.append(sum)
    return r


def rows(table):
    r = []
    for x in range(length):
        sum = sum(table[x][y] for y in range(length))
        r.append(sum)
    return r


def diagonals(table):
    r = []
    sum = 0
    for i in range(length):
        sum += table[i][i]
    r.append(sum)
    r.append(sum)
    sum = sum(table[i][i] for i in range(length).__reversed__())
    r.append(sum)
    r.append(sum)
    return r


def opposites(table):
    r = []
    for i in range(4):
        sum = 0
        sum += table[i][i]
        sum += table[i][1 - i]
        sum += table[1 - i][i]
        sum += table[1 - i][1 - i]
        r.append(sum)
    return r


def pair_groups(table):
    r = []
    for x in range(length - 1):
        for y in range(length - 1):
            print(x, y)
            sum = 0
            sum += table[x][y]
            sum += table[x][y + 1]
            sum += table[x + 1][y]
            sum += table[x + 1][y + 1]
            r.append(sum)
    return r


def groups(table):
    r = []
    for x in range(0, length - 1, 2):
        for y in range(0, length - 1, 2):
            sum = 0
            sum += table[x][y]
            sum += table[x][y + 1]
            sum += table[x + 1][y]
            sum += table[x + 1][y + 1]
            r.append(sum)
    return r


def fitness(table, target_val):
    target_val = list((map(list, zip(*[iter(target_val)] * length))))
    table = list((map(list, zip(*[iter(table)] * length))))

    target = np.array([target_val[0]])
    results = np.array([columns(table), rows(table), diagonals(table), opposites(table), groups(table)])
    dist = sum(sum(distance.cdist(results, target, 'euclidean')))
    return int(dist)


def test():
    table = [
        [10, 3, 13, 19],
        [17, 15, 13, 0],
        [10, 5, 12, 18],
        [8, 22, 7, 8]
    ]
    print(fitness(table, 46))


def brute_force():
    count = 0
    loops_length = (max_num ** (length * length))

    widgets = ['Test: ', Percentage(), ' ', Bar(marker='#', left='[', right=']'),
               ' ', ETA(), ' ', SimpleProgress()]  # see docs for other options

    pbar = ProgressBar(widgets=widgets, maxval=loops_length)
    pbar.start()

    for x in itertools.product(range(max_num), repeat=length * length):
        table = list((map(list, zip(*[iter(x)] * length))))
        # validate(table)
        count += 1

        if count % 10000 == 0:
            pbar.update(count)  # this adds a little symbol at each iteration

    pbar.finish()
