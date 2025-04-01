def stringify(node):
    if node is None:
        return "None"

    result = []

    while node:
        result.append(str(node.data))
        node = node.next

    return " -> ".join(result) + " -> None"
