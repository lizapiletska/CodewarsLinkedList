def linked_list_from_string(s):
    result = Node(None)
    node = result

    values = s.split(" -> ")
    for value in values:
        if value == "None":
            break
        new_node = Node(int(value))
        node.next = new_node
        node = new_node

    return result.next
