# Асинхронная Концепция с Помощью Генераторов (yield)
from time import time, sleep
from os import walk

def clock():
    time_0 = round(time())
    while True:
        if (round(time() - time_0)) % 5 == 0:
            yield ('5 secundes')
        else:
            yield 0


def query():
    for i in walk('C:\\'):
        yield i[0] # Генератор
        # return None # В случае если Явно НЕ прописано ЧТО возвращат Функция

def main():
    data = query()
    message = clock()
    while True:
        d = next(data)
        m = next(message)
        print(d)
        if m: print(m)
        sleep(1)

main()

# python -i file_01_b.py
