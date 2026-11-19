# Задание 1
x = 16

def show():
    x = 6
    print(x)

show()
print(x)

# Вопрос: "Какое x используется внутри функции, а какое снаружи?"
# Ответ: внутри функции используется локальная переменная x = 6, снаружи используется глобальная переменная x = 16.
# Получаем вывод:
# 6
# 16


# Задание 2
print('---------------------------------------------------------')
def total(*args):
    return sum(args)
    pass

print(total(6,7,8))


# Задание 3
print('---------------------------------------------------------')
def person(**kwargs):
    name = kwargs.get("name", "Гость") 
    age = kwargs.get("age", "0") 
    return name, age

print(person(name='Павел', age=17))


# Задание 4
print('---------------------------------------------------------')
def increase(x):
    return x + 1

def apply(func, value):
    return func(value)
    pass

print(apply(increase, 3))


# Задание 5, вывод: 3 2 1
print('---------------------------------------------------------')
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(3)