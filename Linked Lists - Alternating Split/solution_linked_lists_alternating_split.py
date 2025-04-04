class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head:
        raise ValueError()
    if not head.next:
        raise ValueError()

    first, second = head, head.next
    c = Context(first, second)

    while second and second.next:
        first.next, second.next = second.next, second.next.next
        first, second = first.next, second.next

    first.next = None
    return c