from common import *


@record_processing_time
def processing():
    for _ in range(tasks_count()):
        task = retrieve_task()
        result = task_handler(task)
        populate_result(result)


if __name__ == '__main__':
    populate_tasks()
    processing()
    print_results()
