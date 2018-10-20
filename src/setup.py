from setuptools import setup
from task1 import wallet

setup(
    name='knapsack_bellman',
    version='0.7',
    description="Solve of knapsack problem",
    author='Maxim Belov',
    author_email='belovmd@gmail.com',
    url="https://github.com/belovmd",
    scripts=["start_app.py"],
    packages=['task1'],
    long_description=wallet.__doc__
)
