""" Linked Lists - Get Nth Node """

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """ Function for getting a nth element """
    if node is None or index < 0:
        raise IndexError
    if index == 0:
        return node
    while index > 0:
        return get_nth(node.next, index - 1)
