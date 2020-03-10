import math
from collections import namedtuple


def get_ostov(filename):
    Weight = namedtuple('Weight', ['m', 'n', 'weight'])
    f = open(filename, 'r', encoding='utf-8')
    count = int(f.readline())
    numbers = {}
    points = {}
    k = 1
    for line in f:
        p = line.split()
        point = (int(p[0]), int(p[1]))
        numbers[point] = k
        points[k] = point
        k += 1
    d = {}
    for m in points.keys():
        for n in points.keys():
            if m != n and (m, n) not in d.keys() and (n, m) not in d.keys():
                point_m = points[m]
                point_n = points[n]
                d[m, n] = int(math.fabs(point_m[0] - point_n[0]) + math.fabs(point_m[1] - point_n[1]))
                d[(n, m)] = d[(m, n)]
    numbers_in_ostov = [1]
    ostov = {1: []}
    weight = 0
    while len(numbers_in_ostov) != count:
        min = Weight(0, 0, float('inf'))
        for m in numbers_in_ostov:
            for n in points.keys():
                if m != n and n not in numbers_in_ostov and d[(m, n)] < min.weight:
                    min = Weight(m, n, d[(m, n)])
        numbers_in_ostov.append(min.n)
        weight += min.weight
        ostov[min.m].append(min.n)
        ostov[min.n] = [min.m]
    for u in points.keys():
        ostov[u].sort()
        s = ''
        for v in ostov[u]:
            s += '{0} '.format(v)
        print('{0}0'.format(s))
    print(weight)


if __name__ == '__main__':
    get_ostov('in.txt')
