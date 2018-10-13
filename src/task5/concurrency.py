"""Advanced Python courses. Homework#5, Task #1.Maxim Belov.

Outputs sum of prime numbers in the specific range [_, _)
"""
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def add_prime(prime_list, num):
    """Add num in simple_list if it's simple number."""
    if num < 2:
        return

    for div in range(2, num // 2 + 1):
        if num % div == 0:
            return
    prime_list.append(num)


if __name__ == '__main__':
    start = input("Start value: ")
    finish = input("Finish value (not included): ")

    # Lists are thread safe structures in Python
    prime_list = []
    pool = ThreadPoolExecutor(5)
    threads = [pool.submit(add_prime, prime_list, i)
               for i in range(int(start), int(finish))]

    while threads:
        for thread in threads:
            if thread.done():
                threads.remove(thread)
        sleep(0.1)

    print("Simple numbers in range [{start}, {finish}) sum is: {sum}".format(
        start=start,
        finish=finish,
        sum=sum(prime_list)
    ))
