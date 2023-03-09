# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def degree(number_one, number_two):
#     if number_two == 1:
#         return number_one
#     return number_one * degree(number_one, number_two - 1)


# number_one = int(input("Введите первое число: "))
# number_two = int(input("Введите второе число: "))

# print(degree(number_one, number_two))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def summ(number_one, number_two):
    if number_two == 0:
        return number_one
    return 1 + summ(number_one, number_two - 1)


number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))

print (summ(number_one, number_two))
