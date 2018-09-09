"""Advanced Python cources. Homework#3, Task #1.Maxim Belov.

Print numbers from 1 to 100 using 2 threads and Lock synchronization mechanism.
"""
import threading


def odd_printer(max_val, odd_lock, even_lock):
    """Print odd numbers from 1 to max_value."""
    for i in range(1, max_val + 1, 2):
        odd_lock.acquire()
        print(i)
        even_lock.release()


def even_printer(max_val, odd_lock, even_lock):
    """Print even numbers from 2 to max_value."""
    for i in range(2, max_val + 1, 2):
        even_lock.acquire()
        print(i)
        odd_lock.release()


if __name__ == '__main__':
    MAX_VAL = 100
    odd_lock = threading.Lock()
    even_lock = threading.Lock()

    odd_thread = threading.Thread(target=odd_printer,
                                  args=(MAX_VAL, odd_lock, even_lock, ))
    even_thread = threading.Thread(target=even_printer,
                                   args=(MAX_VAL, odd_lock, even_lock, ))

    even_lock.acquire()
    odd_thread.start()
    even_thread.start()
