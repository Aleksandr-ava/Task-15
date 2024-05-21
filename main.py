def test_function():
    inner_function()


def inner_function():
    if 1 > 0:
        print('Я в области видимости функции test_function')


test_function()
