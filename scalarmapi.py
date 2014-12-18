import math

f1 = lambda x: (4 - 2.1 * x[0] ** 2 + (x[0] ** 4) / 3) * x[0] ** 2 + x[0] * x[1] + (-4 + 4 * x[1] ** 2) * x[1] ** 2

f2 = lambda x: math.e + 20 - 20 * math.exp(-0.2 * math.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))) \
               - math.exp(0.5 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1])))


def schedule_point(experiment_id, x):
    return


def get_result(experiment_id, x):
    return f2(x)