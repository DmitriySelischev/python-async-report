from time import time

tasks_array = []
results_array = []
_tasks_number = None
_results_number = None

__all__ = [
    'tasks_count',
    'retrieve_task',
    'populate_result',
    'print_results',
    'task_handler',
    'populate_tasks',
    'record_processing_time',
]


def tasks_count():
    global _tasks_number
    if _tasks_number is not None:
        return _tasks_number
    count = len(tasks_array)
    _tasks_number = count
    return count


def results_count():
    global _results_number
    if _results_number is not None:
        return _results_number
    count = len(results_array)
    _results_number = count
    return count


def populate_task(task: int):
    tasks_array.append(task)


def retrieve_task():
    return tasks_array.pop(0)


def populate_result(result: int):
    results_array.append(result)


def print_results():
    tasks = tasks_count()
    results = results_count()
    print(f"{tasks} tasks converted to {results} results")


def task_handler(task: int) -> int:
    return _fib(task)


def record_processing_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            end_time = time()
            print(f'Processing taken: {end_time - start_time} seconds')
            raise
        end_time = time()
        print(f'Processing taken: {end_time - start_time} seconds')
        return result

    return wrapper


def populate_tasks():
    for i in range(64):
        populate_task(30)
    tasks_count()


def _fib(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return _fib(n - 1) + _fib(n - 2)
    return 0
