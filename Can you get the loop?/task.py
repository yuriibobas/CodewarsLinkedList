""" Can you get the loop? """

class Node:
    """ Node """
    def __init__(self, next = None):
        self.next = next

def loop_size(node):
    """ Class for getting the size of the loop """
    visited = set()
    current = node
    while current:
        if current in visited:
            length_of_loop = 1
            start_of_loop = current
            current = current.next
            while current:
                if current == start_of_loop:
                    return length_of_loop
                length_of_loop += 1
                current = current.next
        visited.add(current)
        current = current.next
