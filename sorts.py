from math import log, floor
from typing import TypeVar

T = TypeVar('T', int, float, str) # allows for typehinting unknown types

def bubble_sort(arr: list[T]) -> list[T]:
    '''
    perform the bubble sort algorithm
    :arr: the list of items
    :returns: a sorted list of items
    '''
    result = arr[:] # shallow copy list
    size = len(arr) # size of list
    for i in range(size): # iterate over numbers 0 thru size - 1
        for j in range(size - i - 1): # iterate over numbers thru size -i - 2
            if result[j] > result[j + 1]: # if the first item is more than the second
                result[j], result[j + 1] = result[j + 1], result[j] # swap them
    return result

def merge(a: list[T], b: list[T]) -> list[T]:
    '''
    merge two sorted lists
    :a: the first list
    :b: the second list
    :returns: a list containing all of the elements of the two arguments sorted
    '''
    result = [] # create empty list
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]: # if top item in first is less than top item in second
            result.append(a.pop(0)) # remove from first list and add to result
        else: # otherwise
            result.append(b.pop(0)) # remove from second list and add to result
    # at this point either a or b is empty
    if len(a) == 0: # a is empty
        while len(b) > 0: # while b is not empty
            result.append(b.pop(0)) # remove from second list and add to result
    else: # b is empty
        while len(a) > 0: # while a is not empty
            result.append(a.pop(0)) # remove from first list and add to result
    return result

def merge_sort(arr: list[T]) -> list[T]:
    '''
    perform the merge sort algorithm
    :arr: the list to sort
    :returns: the sorted list
    '''
    size = len(arr) # size of list
    if size <= 1: # if there is one element in list or empty
        return arr[:] # return a shallow copy of the given list
    return merge( # merge following lists
            merge_sort(arr[:size // 2]), # sort first half of list
            merge_sort(arr[size // 2:]) # sort second half
            )

def selection_sort(arr: list[T]) -> list[T]:
    '''
    Sorts a list using selection sort
    Type T must have < operator imlemented
    :arr: the list to be sorted
    :returns: a sorted list
    '''
    size = len(arr)
    if size <= 1:
        return arr[:] # return shallow copy of list
    arr = arr[:] # shallow copy list
    for i in range(0, size): # cycle over i from 0 to size - 1
        smallest_idx = i # smallest size starts at first index
        for j in range(i + 1, size): # cycle over j from i + 1 to size - 1
            if arr[j] < arr[smallest_idx]: # if current val is smaller
                smallest_idx = j # set current to smallest
        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i] # swap smallest and first
    return arr

def radix_sort(arr: list[int], base: int = 2) -> list[int]:
    '''
    Sorts a list using radix sort
    :arr: the list to be sorted
    :returns: a sorted list
    '''
    size = len(arr) # size of array
    result = arr[:] # shallow copy array
    buckets: list[list[int]] = [[] for _ in range(base)] # create empty buckets
    highest_power = max(map(lambda x: floor(log(x, base)) if x != 0 else 1, arr)) + 1 # find highest power of base
    for i in range(0, highest_power): # cycle from 0 to highest power
        divisor = base ** i # the power of the current base
        mod = base ** (i + 1) # one more than the power of the current base
        for item in result:
            buckets[item % mod // divisor].append(item) # group into buckets
        result.clear() # clear result
        for bucket in buckets: # pull out of buckets
            while len(bucket) > 0:
                result.append(bucket.pop(0)) # put into result
    return result

def radix_sort_in_place(arr: list[int], base: int = 10) -> list[int]:
    '''
    Sorts a list using radix sort in place
    honestly idk if this can legally be called radix
    :arr: the list to be sorted
    :returns: a sorted list
    '''
    size = len(arr) # size of array
    result = arr[:] # shallow copy array
    highest_power = max(map(lambda x: floor(log(x, base)) if x != 0 else 1, arr)) + 1 # find highest power of base
    for i in range(0, highest_power): # cycle from 0 to highest power
        divisor = base ** i # the power of the current base
        mod = base ** (i + 1) # one more than the power of the current base
        for j in range(size):
            for k in range(j, 0, -1):
                if (result[k - 1] % mod // divisor) > (result[k] % mod // divisor):
                    result[k], result[k - 1] = result[k -1], result[k]
                else:
                    break
    return result

def insertion_sort(arr: list[int]) -> list[int]:
    '''
    sorts a list using insertion sort
    :arr: the list to be sorted
    :returns: a sorted list
    '''
    result = arr[:]
    size = len(result)
    for i in range(size):
        for j in reversed(range(i)):
            if result[j] < result[j + 1]:
                break
            result[j], result[j + 1] = result[j + 1], result[j]
    return result
