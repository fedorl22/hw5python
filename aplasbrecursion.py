# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

a = int(input('Введите число А:' ))
b = int(input('Введите число В:' ))
def m_sum_n(m,n):
    if n==0:
        return m
    else:
        return m_sum_n(m,n-1) + 1

print(m_sum_n(a,b))