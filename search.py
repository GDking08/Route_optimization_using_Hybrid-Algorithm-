import heapq

def a_star_expansion(nodes_dict, start_node, end_node, threshold_factor):
    threshold = threshold_factor * start_node.heuristic(end_node)
    print("Threshold: ", threshold)

    for node in nodes_dict.values():
        node.set_g_cost(float('inf'), end_node)

    open_list = [(0 + start_node.heuristic(end_node), 0, start_node)]  # (f(n), g(n), node)
    start_node.set_g_cost(0, end_node)

    expanded_nodes = set()  # Set of nodes we expand
    visited = set()  # Set of visited nodes
    threshold_reached_nodes = []

    while open_list:
        _, g_n, current_node = heapq.heappop(open_list)

        if current_node in visited:
            continue
        
        visited.add(current_node)
        expanded_nodes.add(current_node)

        if current_node.node_id == end_node.node_id:
            print("End Node Reached in Expansion!")
            continue

        if current_node.f_cost > threshold:
            threshold_reached_nodes.append(current_node)
            continue

        for neighbor, edge_weight in current_node.neighbors:
            if neighbor in visited:
                continue

            new_g_n = g_n + edge_weight
            if new_g_n < neighbor.g_cost:
                neighbor.set_g_cost(new_g_n, end_node)
                heapq.heappush(open_list, (neighbor.f_cost, new_g_n, neighbor))

    print("Threshold Exceeded Nodes: ", len(threshold_reached_nodes))
    return expanded_nodes, threshold_reached_nodes