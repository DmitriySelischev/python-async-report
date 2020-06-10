import threading
from queue import Empty, SimpleQueue

from common import *


def thread_main(work_queue: SimpleQueue, results_queue: SimpleQueue):
    while True:
        try:
            task = work_queue.get(block=False)
        except Empty:
            break
        result = task_handler(task)
        results_queue.put(result)


@record_processing_time
def processing():
    threads = []
    tasks_queue = SimpleQueue()
    results_queue = SimpleQueue()

    for _ in range(16):
        thread = threading.Thread(target=thread_main, args=(tasks_queue, results_queue,))
        threads.append(thread)

    for _ in range(tasks_count()):
        task = retrieve_task()
        tasks_queue.put(task)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for _ in range(results_queue.qsize()):
        result = results_queue.get(block=False)
        populate_result(result)


if __name__ == '__main__':
    populate_tasks()
    processing()
    print_results()
