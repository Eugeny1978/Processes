# Синхронное Выполнение
from time import time, sleep
from os import walk

def clock():
    time_0 = round(time())
    while True:
        if (round(time() - time_0)) % 5 == 0:
            print('5 secundes')
            sleep(1)

def query():
    for i in walk('C:\\'):
        print(i[0])

def main():
    query()
    clock() # НЕ выполнится НИКОГДА - тк в предыдущ функ реализован бесконечный цикл


main()
