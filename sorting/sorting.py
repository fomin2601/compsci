from datastructure.heap import MinHeap, MaxHeap
import random


def merge_sort(arr: list) -> list:
    """
    Sorting array by merge sort

    :param arr: array to sorting
    :return: sorted array
    """
    n = len(arr)

    if n <= 1:
        return arr

    left = merge_sort(arr[:n // 2])
    right = merge_sort(arr[n // 2:])

    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """
    Merge to sorted arrays in one sorted array

    :param left: first sorted array
    :param right: second sorted array
    :return: sorted array
    """
    res = []
    i, j = 0, 0

    while i < len(left) or j < len(right):
        if j == len(right) or i < len(left) and left[i] < right[j]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1

    return res


def heap_sort(arr: list, ascending=True):
    """
    Sort array inplace in chosen order by heap sort. Create heap from array and iteratively pop min value

    :param arr: array to sorting
    :param ascending: if True, array will be sorted in ascending order
    """
    if ascending:
        heap = MinHeap(arr)
    else:
        heap = MaxHeap(arr)

    for i in range(len(arr)):
        arr[i] = heap.pop_min()


def quick_sort(arr: list):
    """
    Sort array inplace via quick sort algorithm

    :param arr: array to sorting
    """
    _quick_sort_inplace(arr, 0, len(arr) - 1)


def _quick_sort_inplace(arr: list, left: int, right: int):
    """
    Sort array inplace via quick sort algorithm

    :param arr: array to sorting
    :param left: index of first element
    :param right: index of last element
    """
    if right - left <= 1:
        return

    x = arr[random.randint(left, right)]
    mid_idx = _split(arr, left, right, x)
    _quick_sort_inplace(arr, left, mid_idx - 1)
    _quick_sort_inplace(arr, mid_idx, right)


def _split(arr: list, left: int, right: int, x: int) -> int:
    """
    Find middle index of array to split it like this:
    all elements of array[:middle_index] less than array[x]
    all elements of array[middle_index] greater or equivalent than array[x]

    :param arr: array to splitting
    :param left: index of first element
    :param right: index of last element
    :param x: value x to compare elements
    """
    mid = left
    for i in range(left, right + 1):
        if arr[i] < x:
            arr[i], arr[mid] = arr[mid], arr[i]
            mid += 1

    return mid
