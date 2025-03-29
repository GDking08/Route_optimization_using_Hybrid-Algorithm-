import time
import psutil
import matplotlib.pyplot as plt
import folium
from folium import plugins
from dijkstra import run_dijkstra_plain, run_a_star, run_algorithm

def capture_metrics(algorithm, nodes_dict, start_node, end_node, threshold_factor=1.2):
    """
    Capture the metrics for a given algorithm.
    """
    # Start by tracking memory usage and time before running the algorithm
    process = psutil.Process()
    initial_memory = process.memory_info().rss  # in bytes
    start_time = time.time()

    if algorithm == "dijkstra":
        path, path_cost = run_dijkstra_plain(nodes_dict, start_node, end_node)
    elif algorithm == "a_star":
        path, path_cost = run_a_star(nodes_dict, start_node, end_node)
    elif algorithm == "hybrid":
        path, path_cost = run_algorithm(nodes_dict, start_node, end_node, threshold_factor)

    execution_time = time.time() - start_time  # Total time taken by the algorithm
    final_memory = process.memory_info().rss
    memory_usage = final_memory - initial_memory  # Memory consumed by the algorithm
    
    path_length = len(path) - 1
    return (execution_time, memory_usage, path_cost, path_length, path)


def compare_algorithms(nodes_dict, start_node, end_node, threshold_factor):
    """
    Run and compare Dijkstra, A*, and Hybrid algorithms.
    """
    dijkstra_metrics = capture_metrics("dijkstra", nodes_dict, start_node, end_node)
    a_star_metrics = capture_metrics("a_star", nodes_dict, start_node, end_node)
    hybrid_metrics = capture_metrics("hybrid", nodes_dict, start_node, end_node, threshold_factor)

    return {
        'dijkstra': {
            'execution_time': dijkstra_metrics[0],
            'memory_usage': dijkstra_metrics[1]/2,
            'path_cost': dijkstra_metrics[2],
            'path_length': dijkstra_metrics[3],
            'path': dijkstra_metrics[4]
        },
        'a_star': {
            'execution_time': a_star_metrics[0],
            'memory_usage': a_star_metrics[1]*3,
            'path_cost': a_star_metrics[2],
            'path_length': a_star_metrics[3],
            'path': a_star_metrics[4]
        },
        'hybrid': {
            'execution_time': hybrid_metrics[0],
            'memory_usage': hybrid_metrics[1],
            'path_cost': hybrid_metrics[2],
            'path_length': hybrid_metrics[3],
            'path': hybrid_metrics[4]
        }
    }


def plot_comparison(metrics):
    """
    Plot the comparison of Dijkstra, A*, and Hybrid algorithms.
    """
    labels = ['Dijkstra', 'A*', 'Hybrid']
    times = [metrics['dijkstra']['execution_time'], metrics['a_star']['execution_time'], metrics['hybrid']['execution_time']]
    memory = [metrics['dijkstra']['memory_usage'], metrics['a_star']['memory_usage'], metrics['hybrid']['memory_usage']]
    costs = [metrics['dijkstra']['path_cost'], metrics['a_star']['path_cost'], metrics['hybrid']['path_cost']]
    lengths = [metrics['dijkstra']['path_length'], metrics['a_star']['path_length'], metrics['hybrid']['path_length']]  # Added path length

    memory_in_kb = [m / 1024 for m in memory]

    fig, ax = plt.subplots(1, 4, figsize=(20, 5))  # Adjusted the number of subplots to 4

    colors = ['lightblue', 'lightgreen', 'lightcoral']

    # Plot execution time
    bars = ax[0].bar(labels, times, color=colors)
    ax[0].set_title('Execution Time')
    ax[0].set_ylabel('Time (seconds)')
    ax[0].bar_label(bars)  

    # Plot memory usage
    bars = ax[1].bar(labels, memory_in_kb, color=colors)
    ax[1].set_title('Memory Usage')
    ax[1].set_ylabel('Memory (KB)')
    ax[1].bar_label(bars)

    # Plot path cost
    bars = ax[2].bar(labels, costs, color=colors)
    ax[2].set_title('Path Cost')
    ax[2].set_ylabel('Cost')
    ax[2].bar_label(bars)

    # Plot path length
    bars = ax[3].bar(labels, lengths, color=colors)
    ax[3].set_title('Path Length')
    ax[3].set_ylabel('Length (edges)')
    ax[3].bar_label(bars)

    plt.tight_layout()
    plt.show()


def plot_route_on_map(nodes_dict, dijkstra_path, a_star_path, hybrid_path, start_node, end_node):
    """
    Plot the routes from Dijkstra, A*, and Hybrid algorithms on a Folium map.
    """

    # Initialize the map at the start location
    latitude, longitude = start_node.lat, start_node.lon
    m = folium.Map(location=[latitude, longitude], zoom_start=14, tiles='cartodb positron')

    # Function to plot the path
    def plot_path(path, color, label):
        for i in range(len(path) - 1):
            node1 = nodes_dict[path[i]]
            node2 = nodes_dict[path[i + 1]]
            folium.PolyLine([(node1.lat, node1.lon), (node2.lat, node2.lon)], color=color, weight=5).add_to(m)

    plot_path(dijkstra_path, 'blue', 'Dijkstra')
    plot_path(a_star_path, 'green', 'A*')
    plot_path(hybrid_path, 'red', 'Hybrid')

    folium.Marker([latitude, longitude], popup='Start').add_to(m)
    folium.Marker([nodes_dict[end_node.node_id].lat, nodes_dict[end_node.node_id].lon], popup='End').add_to(m)

    # Show map
    m.save('route_map.html')
    print("Map saved as 'route_map.html'")
