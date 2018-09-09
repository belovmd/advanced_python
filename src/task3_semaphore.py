"""Advanced Python courses. Homework#3, Task #3.Maxim Belov.

Print numbers from 1 to 100 using 2 threads and Semaphore synchronization
mechanism.
"""
import threading


def odd_printer(max_val, even_semaphore, odd_semaphore):
    """Print odd numbers."""
    for i in range(1, max_val + 1, 2):
        odd_semaphore.acquire()
        print(i)
        even_semaphore.release()


def even_printer(max_val, even_semaphore, odd_semaphore):
    """Print even numbers."""
    for i in range(2, max_val + 1, 2):
        even_semaphore.acquire()
        print(i)
        odd_semaphore.release()


if __name__ == '__main__':
    MAX_VAL = 100
    even_semaphore = threading.Semaphore(1)
    odd_semaphore = threading.Semaphore(1)

    odd_thread = threading.Thread(target=odd_printer,
                                  args=(MAX_VAL,
                                        even_semaphore,
                                        odd_semaphore, ))

    even_thread = threading.Thread(target=even_printer,
                                   args=(MAX_VAL,
                                         even_semaphore,
                                         odd_semaphore, ))
    odd_thread.start()
    even_thread.start()

    # Start execution
    odd_semaphore.release()
