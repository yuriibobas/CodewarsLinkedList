""" Swap Node Pairs In Linked List """

class Node:
    """ Node """
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """ Function for swaping node pairs in linked list"""
    if head is None or head.next is None:
        return head
    current = head
    head = head.next
    prev = current
    while current and current.next:
        first = current
        second = current.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        current = first.next
    return head
