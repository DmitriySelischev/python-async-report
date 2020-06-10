import asyncio

from common import *


def task_generator():
    count = tasks_count()
    for _ in range(count):
        yield retrieve_task()


async def handle_result(result):
    populate_result(result)


async def handle_task(task):
    result = task_handler(task)
    await handle_result(result)


async def processing():
    tasks = [asyncio.create_task(handle_task(t)) for t in task_generator()]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    populate_tasks()
    loop = asyncio.get_event_loop()


    # This is just to reuse our recording time decorator
    @record_processing_time
    def process_loop():
        loop.run_until_complete(processing())


    process_loop()
    loop.close()
    print_results()
