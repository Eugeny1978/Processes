# Асинхронная Концепция с Помощью библиотеки asyncio
# Формирование коротинов (асинхронных потоков) через класс asyncio.TaskGroup()
import asyncio

async def print_1():
    print('Print 1')

async def print_2():
    await asyncio.sleep(10)
    print('Print 2')

async def print_3():
    print('Print 3')

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(print_1())
        tg.create_task(print_2())
        tg.create_task(print_3())


asyncio.run(main())
