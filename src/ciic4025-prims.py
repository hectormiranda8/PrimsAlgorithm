from collections import defaultdict
import heapq

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
    'C': {'A': 3, 'B': 12, 'F': 5},
    'D': {'B': 10, 'E': 7},
    'E': {'B': 4, 'D': 7, 'F': 16},
    'F': {'C': 5, 'E': 16, 'G': 9},
    'G': {'F': 9},
}


def create_spanning_tree(graph, root_node):
    mst = defaultdict(set)      # Minimum Spanning Tree set
    explored = {root_node}      # Set containing explored nodes
    edge_nodes = [              # Array containing all linked nodes to the root node
                                # with its corresponding weights
        (weight, root_node, linked_node)
        for linked_node, weight in graph[root_node].items()
    ]
    heapq.heapify(edge_nodes)   # Turn edge_nodes into a heap array
    while edge_nodes:           # While there's something in the heap do:
        weight, from_node, to_node = heapq.heappop(edge_nodes)
        if to_node not in explored: # For all unexplored edges do:
            explored.add(to_node)       # Add node to the explored set
            mst[from_node].add(to_node) # Heap is sorted, therefore we can set the
                                        # to_node as the linked node for the from_node
            for next_node, weight in graph[to_node].items():
                                        # Check which nodes we have to explore from the
                                        # to_node that now will become the from_node
                if next_node not in explored:
                                        # If node is not explored, then we have to explore it
                    heapq.heappush(edge_nodes, (weight, to_node, next_node))

    return mst


print(dict(create_spanning_tree(example_graph, 'D')))
# Output: {'D': {'E'}, 'E': {'B'}, 'B': {'A'}, 'A': {'C'}, 'C': {'F'}, 'F': {'G'}}
