from datastructure.heap import MinHeap, MaxHeap


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
