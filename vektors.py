

def summ(a, b):
    return a[0] + b[0], a[1] + b[1]


def razn(a, b):
    return a[0] - b[0], a[1] - b[1]


def vekt_scalar(a, b):
    return a[0] * b, a[1] * b


def vekt_vekt(a, b):
    return a[0] * b[0], a[1] * b[1]


def lenght(a):
    return (a[0] ** 2 + a[1] ** 2) ** 0.5


def vekt_plus(a, b):
    one = (b - lenght(a)) / (a[0] + a[1])
    amodif = a[0] + (one * a[0]), a[1] + (one * a[1])
    print(amodif[0] / amodif[1])
    return amodif


print(vekt_plus((3, 4), 4))
