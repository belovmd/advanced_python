"""Advanced Python cources. Homework#8, Task #1.Maxim Belov.

Count performance for counting n'th fibonacci number using
C extension, cython, python.

Results:
Python solution: 0.03950148640599946
C extension solution: 0.00038722610200420603
Cython solution: 0.00575604020800165
"""

import fib_count_c
import fib_cython
import timeit


def fib_count(n=20):
    value = fib_count(n - 1) + fib_count(n - 2) if n > 1 else n
    return value


TEST_VALUE = 25
COUNT_VALUE = 100
REPEAT = 5

fib_count_c.fib_count(TEST_VALUE)
fib_cython.fib(TEST_VALUE)

times = (timeit.repeat('fib_count(TEST_VALUE)',
                       repeat=REPEAT,
                       number=COUNT_VALUE,
                       globals=globals()))
print("Python solution:", sum(times) / (REPEAT * COUNT_VALUE))

times = (timeit.repeat('fib_count_c.fib_count(TEST_VALUE)',
                       repeat=REPEAT,
                       number=COUNT_VALUE,
                       globals=globals()))
print("C extension solution:", sum(times) / (REPEAT * COUNT_VALUE))

times = (timeit.repeat('fib_cython.fib(TEST_VALUE)',
                       repeat=REPEAT,
                       number=COUNT_VALUE,
                       globals=globals()))
print("Cython solution:", sum(times) / (REPEAT * COUNT_VALUE))
