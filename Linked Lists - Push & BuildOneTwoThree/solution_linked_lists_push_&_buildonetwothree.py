from preloaded import Node

def push(head, data):
    node = Node(data)
    node.next = head if head is not None else None

    return node

def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)

    return chained

