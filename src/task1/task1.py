"""Advanced Python cources. Homework#6, Task #1.Maxim Belov.

Download a bunch  of files:
using aiohttp, syncio
using common threads
Benchmark performance in both cases time and put results into the
PR description.
"""
import asyncio
import requests
import socket
import threading
import time

import aiohttp


ITEMS_LIST = [
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc2.tar.xz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc2.tgz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tar.xz",
    "https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tgz",
]


async def get_item(client, item):
    url = item
    async with client.get(url) as resp:  # <4>
        assert resp.status == 200
        return await resp.read()


@asyncio.coroutine
def download_one(client, item):
    response = yield from get_item(client, item)
    return response


async def download_many(loop, items_list):
    tcpconnector = aiohttp.TCPConnector(family=socket.AF_INET)
    async with aiohttp.ClientSession(connector=tcpconnector) as client:
        to_do = [download_one(client, item) for item in items_list]
        res = await asyncio.gather(*to_do)
    return res


def download_file(item):
    resp = requests.get(item)
    return resp.content


def download_threads(items_list):
    for i in range(len(items_list)):
        t = threading.Thread(target=download_file, args=(items_list[i],))
        t.start()
        t.join()


def start_async():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_many(loop, ITEMS_LIST))
    loop.close()


def start_threads():
    download_threads(ITEMS_LIST)


if __name__ == '__main__':
    start_time = time.time()
    start_async()
    finish_time = time.time()
    print("Async time: ", finish_time - start_time)

    start_time = time.time()
    start_threads()
    finish_time = time.time()
    print("Threads time: ", finish_time - start_time)
