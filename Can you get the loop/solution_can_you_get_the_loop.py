def loop_size(node):
    visited_nodes = {}
    while node not in visited_nodes:
        visited_nodes[node] = len(visited_nodes)
        node = node.next
    return len(visited_nodes) - visited_nodes[node]