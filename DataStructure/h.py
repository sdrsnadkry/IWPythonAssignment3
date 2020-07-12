graph = {
    'a': {'b': 10, 'c': 3},
    'b': {'c': 1, 'd': 2},
    'c': {'b': 4, 'd': 8, 'e': 2},
    'd': {'e': 7},
    'e': {'d': 9}
}


def dijkstra(graph, start, goal):
    shortest_distance = {}  # records cost to reach that node and keeps updating
    track_predecessor = {}  # track path that lead to this node
    unseen_nodes = graph  # to iterate entire graph and pops in every iterations
    infinity = 99999
    track_path = []  # to trace back to source node

    # Assign cost to first node as 0 and all other node as infinity
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # Iterate through entire graph
    while unseen_nodes:
        min_distance_node = None  # initially there is no any minimum distance node

        for node in unseen_nodes:
            if min_distance_node is None:  # which is true from above expression
                min_distance_node = node  # assign start node as min distance node initially
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node  # change min distance node to node with smaller cost than prev node

        path_options = graph[min_distance_node].items()  # find all possible path of the min distance node

        # main part of the algorithm, telling when we are supposed to update cost of particular node
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node  # track path that is leading us to particular node
                # from min distance node we have gone to child node
        unseen_nodes.pop(min_distance_node)  # remove the path that is already travelled as it is greedy algorithm

    # tracing back the path considering current node as goal node until we reach start node
    current_node = goal

    while current_node != start:
        try:
            track_path.insert(0, current_node)
            current_node = track_predecessor[current_node]  # finds previous node each time
        except KeyError:
            print('Path is not reachable')
            break
    track_path.insert(0, start)  # start node has no predecessor
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('With Path ' + str(track_path))


dijkstra(graph, 'b', 'e')
