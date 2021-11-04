from math import exp, sqrt


def func(a, t):
    return (a * exp(-t) + (4 - 3 * a) * exp(-2 * t) + (2 * a - 4) * exp(-4 * t))


def derivative(a, t):
    return (-a * exp(-t) - (4 - 3 * a) / 2 * exp(-2 * t) - (2 * a - 4) / 4 * exp(-4 * t))


def get_time(value):
    return value * 60 // 60, value * 60 % 60


def print_average(a):
    res = 0
    t = 0
    i = 0
    deviation = 0
    while i < 99.9999:
        res += (func(a, t) / 10) * t
        t += 0.001
        i += func(a, t) / 10
    res /= 99.9999
    res += 1./60
    print("Average return time: %dm %02ds" % get_time(res))
    t = 0
    while t < 100:
        deviation += (pow(t - res, 2) * (func(a, t) / 10))
        t += 0.001
    deviation /= 100
    deviation = sqrt(deviation)
    print("Standard deviation: %.3f" % deviation)


def time_on_percent(a, percent):
    res = 0.0
    for i in range(1000):
        res += func(a, i / 100)
        print(res, percent, i / 100)
        if res >= percent:
            return i / 100
    return -1


def prob_after_time(a, time):
    return ((derivative(a, time) - derivative(a, 0)) * 100)

