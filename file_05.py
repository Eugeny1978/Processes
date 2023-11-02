# Асинхронная Концепция с Помощью библиотеки asyncio
# Формирование коротинов (асинхронных потоков) через класс asyncio.TaskGroup()
import asyncio
from time import time

async def print_sec(sec):
    await asyncio.sleep(sec)
    print(f'Print {sec}')

# Если выполнить синхронным кодом, то: 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15 = 120 сек
async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print_sec(i))


start = time()
asyncio.run(main())
print(f'Время выполнения: {round(time() - start, 4)} sec')