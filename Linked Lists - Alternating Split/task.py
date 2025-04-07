""" Linked Lists - Alternating Split """

class Node(object):
    """ Node """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """ Context """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """ Function for alternating splitting """
    if head is None or head.next is None:
        raise ValueError
    first = head
    second = head.next
    current = second.next
    first_current = first
    second_current = second
    while current:
        first_current.next = current
        first_current = first_current.next
        if current.next:
            second_current.next = current.next
            current = current.next.next
            second_current = second_current.next
        else:
            current = current.next
    if first_current:
        first_current.next = None
    if second_current:
        second_current.next = None
    return Context(first, second)
