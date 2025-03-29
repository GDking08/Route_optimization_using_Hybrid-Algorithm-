# graph.py

import osmnx as ox
import networkx as nx
import math

class Node:
    def __init__(self, node_id, lat, lon):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon
        self.g_cost = float('inf')  # g(n): Cost to reach this node
        self.f_cost = float('inf')  # f(n): Total estimated cost (g(n) + h(n))
        self.neighbors = []
        
    def add_neighbor(self, neighbor_node, edge_weight):
        self.neighbors.append((neighbor_node, edge_weight))

    def set_g_cost(self, cost, target_node):
        self.g_cost = cost
        self.f_cost = self.g_cost + self.heuristic(target_node)

    def deg_to_rad(self, deg):
        """Convert degrees to radians."""
        return deg * (math.pi / 180)

    def heuristic(self, target_node):
        """Calculate the Haversine distance to another node."""
        R = 6371000
        
        lat1 = self.deg_to_rad(self.lat)
        lon1 = self.deg_to_rad(self.lon)
        lat2 = self.deg_to_rad(target_node.lat)
        lon2 = self.deg_to_rad(target_node.lon)

        # Differences in coordinates
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine formula
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance in meters
        distance = R * c
        return distance

    def __repr__(self):
        return f"Node({self.node_id}, {self.lat}, {self.lon})"


def build_graph_from_osm(place_name, network_type='all'):
    G = ox.graph_from_place(place_name, network_type=network_type)

    nodes_dict = {}
    for node_id, data in G.nodes(data=True):
        node = Node(node_id, data['y'], data['x'])
        nodes_dict[node_id] = node

    for u, v, data in G.edges(data=True):
        u_node = nodes_dict[u]
        v_node = nodes_dict[v]
        distance = data['length']
        u_node.add_neighbor(v_node, distance)
        v_node.add_neighbor(u_node, distance)

    return G, nodes_dict

def build_dict_from_graph(graph):
    nodes_dict = {}
    for node_id, data in graph.nodes(data=True):
        node = Node(node_id, data['y'], data['x'])
        nodes_dict[node_id] = node

    for u, v, data in graph.edges(data=True):
        u_node = nodes_dict[u]
        v_node = nodes_dict[v]
        distance = data['length']
        u_node.add_neighbor(v_node, distance)
        v_node.add_neighbor(u_node, distance)

    return nodes_dict


































    # def heuristic_a_star(self, target_node):
    #     """Calculate the Euclidean distance to another node."""
    #     # Convert latitude and longitude to Cartesian coordinates (approximation for small areas)
    #     x1, y1 = self.lat, self.lon
    #     x2, y2 = target_node.lat, target_node.lon

    #     # Euclidean distance formula
    #     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    #     return distance





# def set_g_cost_a_star(self, cost, target_node):
    #     self.g_cost = cost
    #     # Update f_cost based on g_cost and heuristic to target_node (end node)
    #     self.f_cost = self.g_cost + self.heuristic_a_star(target_node)
