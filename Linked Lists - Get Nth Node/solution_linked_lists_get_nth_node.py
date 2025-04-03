from preloaded import Node
 
def get_nth(node, index):
    while index:
        if not node:
            raise Exception()

        node = node.next
        index -= 1

    if node:
        return node
    else:
        raise IndexError()
