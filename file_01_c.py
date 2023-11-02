# Асинхронная Концепция с Помощью библиотеки asyncio
import asyncio

async def print_1():
    print('Print 1')

async def print_2():
    await asyncio.sleep(10)
    print('Print 2')

async def print_3():
    print('Print 3')

async def main():
    task_1 = asyncio.create_task(print_1())
    task_2 = asyncio.create_task(print_2())
    task_3 = asyncio.create_task(print_3())

    # await task_1
    # await task_2
    # await task_3
    # await asyncio.gather(task_1, task_2, task_3)
    tasks = [task_1, task_2, task_3]
    await asyncio.gather(*tasks)


asyncio.run(main())
