from setuptools import Extension
from setuptools import setup

setup(name='fibonacci',
      version='1.0',
      description="Counts fibonacci n'th element",
      ext_modules=[
          Extension('fib_count_c', sources=['fib.c'], py_limited_api=True)
      ])
