""" Linked Lists - Move Node """

class Node(object):
    """ Node """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """ Context """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """ Function for moving node """
    node_to_move = source
    source = source.next
    node_to_move.next = dest
    dest = node_to_move
    return Context(source, dest)
