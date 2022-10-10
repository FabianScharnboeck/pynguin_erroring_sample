import multiprocessing as mp
from typing import List

my_list: List = []


def my_map():
    for i in range(10000):
        my_list.append(i)
    with mp.Pool() as p:
        my_mapped_list: List = p.map_async(func=multiply, iterable=my_list).get()
        print(my_mapped_list)


def multiply(element):
    element_new = element * element
    return element, element_new

