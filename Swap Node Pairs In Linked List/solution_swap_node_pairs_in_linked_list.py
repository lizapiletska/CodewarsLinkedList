from preloaded import Node

def swap_pairs(head):

    if head is None or head.next is None:
        return head

    node_one = head
    node_two = head.next

    rest = swap_pairs(node_two.next)

    node_two.next = node_one
    node_one.next = rest

    return node_two