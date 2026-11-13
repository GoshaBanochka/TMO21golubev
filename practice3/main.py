# вариант 6
# задание 1
g = (x + 6 for x in range(1,3+1))
print(list(g))


# задание 2
def announce(func):
    def wrapper():
        print('Начинаем')
        result = func()
        print('Готово')
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()