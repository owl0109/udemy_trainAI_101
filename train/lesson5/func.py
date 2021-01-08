def func_sample():
    print('==========function==========')
    print('hello world')
    name_printer('田中')
    result = add(3, 5)
    print(result)


def name_printer(name):
    print('こんにちは！' + name + 'さん')


def add(num1, num2):
    return num1 + num2
