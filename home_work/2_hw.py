def task_1():
    a: int = 7
    b: float = 36.6
    c: str = 'Прекрасный день'
    d: list = [1, 2, 3, 4, 5]
    e: bool = True
    print(task_1(type(a), type(b), type(c), type(d), type(e), '\n'))


def task_2() ->list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[:3]
print(task_2(), '\n')

def task_3(a:int) ->int:
    return a ** 2
    print(task_3(9))




