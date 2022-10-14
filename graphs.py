import queue


class Graph:
    # The graph is stored in an adjacency dictionary where each key 
    # represents a node in the graph and each value in the dictionary
    # represents the corresponding key's list of edges
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict

    def breadth_first_search(self):
        queue = []
        visited = []

        for node in self.adjacency_dict:
            if node not in visited:
                visited.append(node)
                queue.append(node)
            while queue:
                current = queue[0]
                queue.pop(0)
                for neighbor in current[0]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)


        return visited