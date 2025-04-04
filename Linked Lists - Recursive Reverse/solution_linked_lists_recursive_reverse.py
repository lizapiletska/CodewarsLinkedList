class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    previous = None

    while head:
        next_node = head.next
        head.next = previous
        previous = head
        head = next_node

    return previous  