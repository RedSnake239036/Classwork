import math


def rectangle(a, b):
    return a * b


def circle(r):
    return math.pi * r ** 2


def triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

