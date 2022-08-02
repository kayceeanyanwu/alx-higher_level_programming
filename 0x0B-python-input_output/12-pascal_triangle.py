#!/usr/bin/python3
""" module that handles pascal traingles """


def pascal_triangle(n):
    """ helper function called by main """

    ans = []
    listo = []

    for i in range(0, n):
        previous = listo
        if i is not 0:
            listo = [1]
        for j in range(1, i):
            listo.append(previous[j - 1] + previous[j])
        listo.append(1)
        ans.append(listo)
    return ans
