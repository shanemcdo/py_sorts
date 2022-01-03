#!/usr/bin/env python3

from sorts import bubble_sort, merge_sort, selection_sort, radix_sort, radix_sort_in_place
from typing import TypeVar, Callable
from random import randint
import time

T = TypeVar('T', int, float, str) # allows for typehinting unknown types

def rand_arr(size: int, min_val: int = 0, max_val: int = 10) -> list[int]:
    '''
    creates a list of random numbers
    :size: size of return list
    :min_val: minimum value for numbers in list
    :max_val: maximum value for numbers in list
    :returns: a list of random numbers
    '''
    return [randint(min_val, max_val) for i in range(size)]

def is_sorted(arr: list[T]) -> bool:
    '''
    print array and check if sorted
    :arr: the list of items
    :returns: True if the list is sorted
    '''
    size = len(arr) # size of array
    if size <= 1: # size is 0 or 1
        return True # with 0 or 1 element there is no order
    for i in range(size - 1): # iterate from 0 to size - 2
        if arr[i + 1] < arr[i]: # if the second term is less than the first term
            return False # the list isnt sorted
    return True # otherwise the list is sorted


def test_sort(sort_func: Callable[[list[int]], list[int]], number_of_items: int = 40, max_val:int = 100, print_lists: bool = True, print_time: bool = True):
    '''
    test to make sure a sort function works
    :sort_func: the function that will return a sorted list
    '''
    print('-' * 10, f'testing {sort_func.__name__}', '-' * 10)
    arr = rand_arr(number_of_items, max_val = max_val) # get random array
    if print_lists:
        print('before:', arr) # show list
    start = time.time()
    arr = sort_func(arr) # sort list
    end = time.time()
    if print_lists:
        print('sorted:', arr) # show array
    if print_time:
        print('time elapsed:', end - start)
    assert is_sorted(arr) # check list

def main():
    '''driver code'''
    t = lambda s: test_sort(s, 10, 10 ** 3, True, True)
    t(bubble_sort)
    t(merge_sort)
    t(selection_sort)
    t(radix_sort)
    t(radix_sort_in_place)

if __name__ == '__main__':
    main() # run the main method
