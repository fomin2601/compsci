class MinHeap:
    """
    Heap with 'less than' condition

    Constructors:
    __init__()

    Methods:
    insert()
    get_min()
    remove_min()
    pop_min()

    Properties:
    heap: list
    """

    def __init__(self, arr=None):
        """
        Constructor.

        :param arr: list or None
        """
        assert type(arr) == list or arr is None, 'Expected list or None'
        self.heap = []

        if arr:
            for elem in arr:
                self.insert(elem)

    def insert(self, x: int):
        """
        Insert new value to the heap and make sift up

        :param x: new value
        """
        assert type(x) == int or type(x) == float, 'Expected int or float value'
        self.heap.append(x)
        idx = len(self.heap) - 1

        while idx > 0 and self.heap[(idx - 1) // 2] > self.heap[idx]:
            self.heap[idx], self.heap[(idx - 1) // 2] = self.heap[(idx - 1) // 2], self.heap[idx]
            idx = (idx - 1) // 2

    def get_min(self):
        """
        Return min value of heap
        """
        assert len(self.heap) > 0, 'Heap is empty'
        return self.heap[0]

    def remove_min(self):
        """
        Remove min value of heap without returning it
        """
        assert len(self.heap) > 0, 'Heap is empty'
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        idx = 0
        while 2 * idx + 1 < len(self.heap):
            sift_idx = 2 * idx + 1
            if 2 * idx + 2 < len(self.heap) and self.heap[2 * idx + 2] < self.heap[sift_idx]:
                sift_idx = 2 * idx + 2

            if self.heap[idx] <= self.heap[sift_idx]:
                break

            else:
                self.heap[idx], self.heap[sift_idx] = self.heap[sift_idx], self.heap[idx]
                idx = sift_idx

    def pop_min(self):
        """
        Remove min value of heap and return it
        """
        assert len(self.heap) > 0, 'Heap is empty'
        res = self.get_min()
        self.remove_min()
        return res


class MaxHeap:
    """
        Heap with 'greater than' condition

        Constructors:
        __init__()

        Methods:
        insert()
        get_min()
        remove_min()
        pop_min()

        Properties:
        heap: list
        """

    def __init__(self, arr=None):
        """
        Constructor.

        :param arr: list or None
        """
        assert type(arr) == list or arr is None, 'Expected list or None'
        self.heap = []

        if arr:
            for elem in arr:
                self.insert(elem)

    def insert(self, x: int):
        """
        Insert new value to the heap and make sift up

        :param x: new value
        """
        assert type(x) == int or type(x) == float, 'Expected int or float value'
        self.heap.append(x)
        idx = len(self.heap)
        while idx > 0 and self.heap[idx] > self.heap[(idx - 1) // 2]:
            self.heap[idx], self.heap[(idx - 1) // 2] = self.heap[(idx - 1) // 2], self.heap[idx]
            idx = (idx - 1) // 2

    def get_max(self):
        """
        Return max value of heap
        """
        assert len(self.heap) > 0, 'Heap is empty'
        return self.heap[0]

    def remove_max(self):
        """
        Remove max value of heap without returning it
        """
        assert len(self.heap) > 0, 'Heap is empty'
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        idx = 0
        while 2 * idx + 2 < len(self.heap):
            sift_idx = 2 * idx + 1
            if 2 * idx + 2 < len(self.heap) and self.heap[2 * idx + 2] >= self.heap[sift_idx]:
                sift_idx = 2 * idx + 2

            if self.heap[idx] >= self.heap[sift_idx]:
                break

            else:
                self.heap[idx], self.heap[sift_idx] = self.heap[sift_idx], self.heap[idx]
                idx = sift_idx

    def pop_max(self):
        """
        Remove max value of heap and return it
        """
        assert len(self.heap) > 0, 'Heap is empty'
        res = self.get_max()
        self.remove_max()
        return res