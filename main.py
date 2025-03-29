import random
import pickle
from graph import build_graph_from_osm, build_dict_from_graph
from metrics import compare_algorithms, plot_comparison, plot_route_on_map

if __name__ == "__main__":
    # Load the graph from OpenStreetMap data

    with open('tn_graph.pkl', 'rb') as graph_file:
        graph = pickle.load(graph_file)

    # place_name = "Tamil Nadu, India"  # Example location
    # graph, nodes_dict = build_graph_from_osm(place_name)
    nodes_dict = build_dict_from_graph(graph)

    print("Total nodes in graph: ", len(graph.nodes))
    print("Total edges in graph: ", len(graph.edges))

    # with open('tn_graph.pkl', 'wb') as graph_file:
    #     pickle.dump(graph, graph_file)

    random.seed(17)

    node_ids = list(nodes_dict.keys())
    start_node_id = random.choice(node_ids)
    end_node_id = random.choice(node_ids)

    while start_node_id == end_node_id:
        end_node_id = random.choice(node_ids)

    start_node = nodes_dict[start_node_id]
    end_node = nodes_dict[end_node_id]

    threshold_factor = 1.5  # Example threshold factor
    
    metrics = compare_algorithms(nodes_dict, start_node, end_node, threshold_factor)

    plot_comparison(metrics)
    plot_route_on_map(nodes_dict, metrics['dijkstra']['path'], metrics['a_star']['path'], metrics['hybrid']['path'], start_node, end_node)
