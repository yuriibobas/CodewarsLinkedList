""" Linked Lists - Remove Duplicates """

class Node(object):
    """ Node """
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """ Function for removing duplicates """
    visited = set()
    current = head
    prev = None
    while current is not None:
        if current.data not in visited:
            visited.add(current.data)
            prev = current
            current = current.next
        else:
            if prev is None:
                head = current.next
            else:
                prev.next = current.next
            current = current.next
    return head
