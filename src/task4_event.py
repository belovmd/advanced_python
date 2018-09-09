"""Advanced Python courses. Homework#3, Task #4.Maxim Belov.

Print numbers from 1 to 100 using 2 threads and Event synchronization
mechanism.
"""
import threading


def odd_printer(max_val, even_event, odd_event):
    """Print odd numbers."""
    for i in range(1, max_val + 1, 2):
        even_event.wait()
        print(i)
        even_event.clear()
        odd_event.set()


def even_printer(max_val, even_event, odd_event):
    """Print even numbers."""
    for i in range(2, max_val + 1, 2):
        odd_event.wait()
        print(i)
        odd_event.clear()
        even_event.set()


if __name__ == '__main__':
    MAX_VAL = 100
    even_event = threading.Event()
    odd_event = threading.Event()

    odd_thread = threading.Thread(target=odd_printer,
                                  args=(MAX_VAL,
                                        even_event,
                                        odd_event,))

    even_thread = threading.Thread(target=even_printer,
                                   args=(MAX_VAL,
                                         even_event,
                                         odd_event,))
    odd_thread.start()
    even_thread.start()

    # Start execution
    even_event.set()
