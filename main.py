from sorting.sorting import merge_sort, heap_sort
from datastructure.linkedlist import ListNode, reverse_linked_list, remove_nth_from_end
from datastructure.heap import MinHeap, MaxHeap


a = [2, 3, 1, 6, 8, 10, 1, 4]
b = [42, 10, 6, 8, 7, 5, 2]
heap = MaxHeap(b)
print(heap.heap)
print(merge_sort(a))
heap_sort(a)
print(a)

node = ListNode(5)
for i in range(4, -1, -1):
    node = ListNode(i, node)

node = reverse_linked_list(node)
node = remove_nth_from_end(node, 3)

while node:
    print(node.val)
    node = node.next_node
