"""
    @author Jay Lee
    A simple utility for handling concurrent operations
    TODO: Start working on this section when I have time.
"""

import concurrent.futures

class Executor(object):
    def __init__(self, task, max_workers=5):
        self.task = task
        self.max_workers = max_workers

    def execute(self, data):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.task, data)


counter = 0


def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1
        print(f"counter: {counter}")


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]

    executor = Executor(increment_counter, max_workers=5000)
    executor.execute(fake_data)


