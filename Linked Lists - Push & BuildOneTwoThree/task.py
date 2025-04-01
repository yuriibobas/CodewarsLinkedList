''' Linked Lists - Push & BuildOneTwoThree '''

class Node:
    """ Node """
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """ Adds node with data to head """
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def build_one_two_three():
    """ Creates and returns a linked list with three nodes: 1 -> 2 -> 3 -> None """
    head = None
    for data in [3, 2, 1]:
        head = push(head, data)
    return head
