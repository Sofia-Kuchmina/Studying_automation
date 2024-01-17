def add(x, y):
    return x + y


print(add(2,2))

print(add('i a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1,1, 1))

print(arg(2, 2))

# print(arg(2, 2, '1', 1))


def rang_arg(a, b, c, d):
    return a + '' + b + '' + c + '' + d


print(rang_arg('1', '2', '3', '4'))

print(rang_arg('1', '2', d='3', c='4'))

def task_1(a=(1, 2, 3, 4)):
    return a[1]

print(task_1())

def task_2(r, pi= 3.14189):
    return pi * r ** 2

print(task_2(2))