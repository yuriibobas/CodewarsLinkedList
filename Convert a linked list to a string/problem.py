""" Convert a linked list to a string """

class Node():
    """ Node """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    """ Function for converting a linked list to a string """
    string = ''
    while node is not None:
        string += str(node.data) + ' -> '
        node = node.next
    string += 'None'
    return string
