"""Advanced Python courses. Homework#3, Task #5.Maxim Belov.

Print numbers from 1 to 100 using 2 threads and Timer synchronization
mechanism.
There are some issues with this implementation:
    1. It will work correctly only for python 3.x for integer DELAY valuse
    because of '|' operator implementation
    2. It will not work correctly if one of threads would be freezed because
    of some OS problems.
    3. This implementation starts 100 threads. Odd_printer produces threads
    that should print odd numbers. Even_printer has the same logic.
"""

import threading

DELAY = 0.1


def odd_printer(max_val, val):
    """Print odd numbers."""
    if val <= max_val:
        print(val)
        threading.Timer(DELAY, odd_printer, args=(max_val, val + 2)).start()


def even_printer(max_val, val):
    """Print even numbers."""
    if val <= max_val:
        print(val)
        threading.Timer(DELAY, even_printer, args=(max_val, val + 2)).start()


if __name__ == '__main__':
    MAX_VAL = 100

    threading.Timer(DELAY / 2, odd_printer, args=(MAX_VAL, 1)).start()
    threading.Timer(DELAY, even_printer, args=(MAX_VAL, 2)).start()
