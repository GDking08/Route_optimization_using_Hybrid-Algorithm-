import heapq
from search import a_star_expansion

def run_dijkstra(nodes_dict, start_node, end_node, expanded_nodes):
    """
    Run Dijkstra's algorithm on the relevant nodes and return the shortest path.
    """
    distances = {node.node_id: float('inf') for node in expanded_nodes}
    predecessors = {node.node_id: None for node in expanded_nodes}
    distances[start_node.node_id] = 0
    
    pq = [(0, start_node)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node.node_id]:
            continue
        
        for neighbor, weight in current_node.neighbors:
            if neighbor not in expanded_nodes:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor.node_id]:
                distances[neighbor.node_id] = new_distance
                predecessors[neighbor.node_id] = current_node.node_id
                heapq.heappush(pq, (new_distance, neighbor))
    
    path = []
    path_cost = 0
    current_node = end_node.node_id
    while current_node is not None:
        path.append(current_node)
        
        predecessor = predecessors[current_node]
        
        if predecessor is not None:
            for neighbor, weight in nodes_dict[current_node].neighbors:
                if neighbor.node_id == predecessor:
                    path_cost += weight
                    break
        
        current_node = predecessor
    
    path.reverse()
    
    return path, path_cost


def run_dijkstra_plain(nodes_dict, start_node, end_node):
    """
    Run Dijkstra's algorithm on the entire graph without any search space optimization.
    This function operates directly on the full graph.
    """
    distances = {node_id: float('inf') for node_id in nodes_dict.keys()}
    predecessors = {node_id: None for node_id in nodes_dict.keys()}
    distances[start_node.node_id] = 0
    
    pq = [(0, start_node)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node.node_id]:
            continue
        
        for neighbor, weight in current_node.neighbors:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor.node_id]:
                distances[neighbor.node_id] = new_distance
                predecessors[neighbor.node_id] = current_node.node_id
                heapq.heappush(pq, (new_distance, neighbor))
    
    path = []
    path_cost = 0
    current_node = end_node.node_id
    while current_node is not None:
        path.append(current_node)
        
        predecessor = predecessors[current_node]
        
        if predecessor is not None:
            for neighbor, weight in nodes_dict[current_node].neighbors:
                if neighbor.node_id == predecessor:
                    path_cost += weight
                    break
        
        current_node = predecessor
    
    path.reverse()
    
    return path, path_cost


def run_a_star(nodes_dict, start_node, end_node):
    """
    Run A* algorithm on the entire graph.
    This function uses both g_cost and h_cost for A* to guide the search.
    """

    start_node.set_g_cost(0, end_node)
    
    open_list = []
    heapq.heappush(open_list, (start_node.f_cost, start_node))  # (f_cost, node)
    
    came_from = {}
    
    while open_list:
        _, current_node = heapq.heappop(open_list)
        
        if current_node == end_node:
            break
        
        for neighbor, weight in current_node.neighbors:
            tentative_g_cost = current_node.g_cost + weight
            
            if tentative_g_cost < neighbor.g_cost:
                neighbor.set_g_cost(tentative_g_cost, end_node)
                came_from[neighbor.node_id] = current_node.node_id
                heapq.heappush(open_list, (neighbor.f_cost, neighbor))  # Push the neighbor into the open list
    
    path = []
    path_cost = 0
    current_node = end_node.node_id
    while current_node != start_node.node_id:
        path.append(current_node)
        
        predecessor = came_from.get(current_node, None)
        
        if predecessor is not None:
            for neighbor, weight in nodes_dict[current_node].neighbors:
                if neighbor.node_id == predecessor:
                    path_cost += weight
                    break
        
        current_node = predecessor
    
    path.append(start_node.node_id)
    path.reverse()
    
    return path, path_cost

def run_algorithm(nodes_dict, start_node, end_node, threshold_factor):
    expanded_nodes, threshold_reached_nodes = a_star_expansion(nodes_dict, start_node, end_node, threshold_factor)
    print("Expanded Nodes after expansion: ", len(expanded_nodes))

    path, path_cost = run_dijkstra(nodes_dict, start_node, end_node, expanded_nodes)

    return path, path_cost
