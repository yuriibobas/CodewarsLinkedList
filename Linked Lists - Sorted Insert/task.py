""" Linked Lists - Sorted Insert """

class Node(object):
    """ Node """
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """ Function for inserting a node with data in a way that makes them sorted """
    node_insert = Node(data)
    if head is None:
        head = node_insert
        return head
    all_data = []
    current = head
    while current is not None:
        all_data.append(current.data)
        current = current.next
    length = len(all_data)
    pos = None
    for i in range(length - 1):
        if all_data[i] < data < all_data[i+1]:
            pos = i+1
            break
    if pos is None:
        if data < all_data[0]:
            pos = 0
        else:
            pos = length
    current = head
    prev = None
    while pos > 0:
        if prev is None:
            prev = head
        else:
            prev = prev.next
        pos -= 1
        current = current.next
    node_insert.next = current
    if prev is not None:
        prev.next = node_insert
    else:
        head = node_insert
    return head
