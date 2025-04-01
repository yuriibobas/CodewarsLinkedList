""" Parse a linked list from a string """

class Node:
    """ Node """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data}, {self.next})'


def linked_list_from_string(s):
    """ Function for parsing a linked list from a string """
    if s == 'None':
        return None
    s = s.split(' -> ')
    head = Node(s[0])
    current = head
    for elem in s[1:]:
        if elem != 'None':
            current.next = Node(elem)
            current = current.next
    return head
