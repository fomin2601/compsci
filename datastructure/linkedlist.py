class ListNode:
    """
    Node of linked list

    Constructors:
    __init__()

    Properties (read only):
    val: int, next_node: ListNode
    """
    __slots__ = ('val', 'next_node')

    def __init__(self, val: int = 0, next_node=None):
        """
        Constructor

        :param val: value in current node
        :param next_node: link to the next node of linked list or None
        """
        assert type(val) == int, 'Parameter "val" should be int value'
        assert type(next_node) == ListNode or next_node is None, 'Expected ListNode object or None'

        self.val = val
        self.next_node = next_node

    def __reversed__(self):
        pass


def reverse_linked_list(head):
    """
    Reverse linked list

    :param head: linked list to reverse
    :return: reversed linked list
    """
    assert type(head) == ListNode or head is None, 'Expected ListNode object or None'
    previous = None
    current = head

    while current:
        current.next_node, previous, current = previous, current, current.next_node

    return previous


def remove_nth_from_end(head, n):
    """
    Removing n'th node from the end of the list and return changed linked list

    :param head: linked list
    :param n: n'th node from the end
    :return: changed linked list
    """
    assert type(head) == ListNode or head is None, 'Parameter "head" should be ListNode object or None'
    assert type(n) == int, 'Parameter "val" should be int value'

    slow = head
    fast = head

    for i in range(n):
        fast = fast.next_node

    if not fast:
        return head.next_node

    while fast.next_node:
        slow = slow.next_node
        fast = fast.next_node

    slow.next_node = slow.next_node.next_node

    return head
