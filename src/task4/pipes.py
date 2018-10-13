"""Advanced Python cources. Homework#4, Task #1.Maxim Belov.

Print numbers from 1 to 100 using 2 processes and Pipes.
"""
from multiprocessing import Pipe
from multiprocessing import Process


def odd_printer(odd_pipe, even_pipe, max_val):
    """Print odd numbers from 1 to max_value."""
    for i in range(1, max_val + 1, 2):
        odd_pipe.recv()
        print(i)
        even_pipe.send(True)


def even_printer(odd_pipe, even_pipe, max_val):
    """Print even numbers from 2 to max_value."""
    for i in range(2, max_val + 1, 2):
        even_pipe.recv()
        print(i)
        odd_pipe.send(True)


if __name__ == '__main__':
    MAX_VAL = 100
    odd_parent, odd_child = Pipe()
    even_parent, even_child = Pipe()

    odd_process = Process(target=odd_printer,
                          args=(odd_parent, even_child, MAX_VAL))
    even_process = Process(target=even_printer,
                           args=(odd_child, even_parent, MAX_VAL))
    odd_process.start()
    even_process.start()

    odd_child.send("Start")
