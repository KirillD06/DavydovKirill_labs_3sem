import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"time: {elapsed}")
        return False


@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"time: {elapsed}")


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(2.5)
    
    with cm_timer_2():
        time.sleep(2.5)
