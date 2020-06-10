import multiprocessing

from common import *


def task_generator():
    count = tasks_count()
    for _ in range(count):
        yield retrieve_task()


@record_processing_time
def processing():
    pool = multiprocessing.Pool(16)
    results = pool.map(task_handler, task_generator())
    for result in results:
        populate_result(result)


if __name__ == '__main__':
    populate_tasks()
    processing()
    print_results()
