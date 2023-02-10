# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


a = int(input('Введите число А:' ))
b = int(input('Введите число В:' ))
def m_degree_n(m,n):
    if n==0:
        return 1
    else:
        return m * m_degree_n(m,n-1)

print(m_degree_n(a,b))

