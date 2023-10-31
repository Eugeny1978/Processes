# Синхронное Выполнение Кода
from time import sleep

def print_1():
    print('Print 1')

def print_2():
    sleep(10)
    print('Print 2')

def print_3():
    print('Print 3')

def main():
    print_1()
    print_2()
    print_3()


main()
