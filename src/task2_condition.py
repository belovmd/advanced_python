"""Advanced Python courses. Homework#3, Task #2.Maxim Belov.

Print numbers from 1 to 100 using 2 threads and Condition synchronization
mechanism.

To be honest there are some issues with this implementation:
    1. this synchronization relies on notifyAll() method queues waiting
    threads and calls them using FIFO order.
    2. It would print in unpredictable order if odd_printer thread won't
    acquire lock and went into wait() while main thread sleeps for 2 seconds
"""

import threading
import time


def odd_printer(max_val, printed_condition):
    """Print odd numbers."""
    for i in range(1, max_val + 1, 2):
        with printed_condition:
            printed_condition.wait()
            print(i)
            with printed_condition:
                printed_condition.notifyAll()


def even_printer(max_val, printed_condition):
    """Print even numbers."""
    for i in range(2, max_val + 1, 2):
        with printed_condition:
            printed_condition.wait()
            print(i)
            with printed_condition:
                printed_condition.notifyAll()


if __name__ == '__main__':
    MAX_VAL = 100
    printed_condition = threading.Condition()

    odd_thread = threading.Thread(target=odd_printer,
                                  args=(MAX_VAL,
                                        printed_condition,))

    even_thread = threading.Thread(target=even_printer,
                                   args=(MAX_VAL,
                                         printed_condition,))
    odd_thread.start()
    # This sleep is a cheat but it would be too monstrous to set the right
    # threads start order using conditions
    time.sleep(2)
    even_thread.start()

    # Start printing
    with printed_condition:
        printed_condition.notifyAll()
