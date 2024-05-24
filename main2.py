def test_function(a):
    d = a * 2

    def inner_function():
        if d % 2 == 0:
            print('Я в области видимости функции test_function')

    inner_function()
    return d


b = test_function(4)
print(b)
