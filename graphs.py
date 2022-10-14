import queue


class Graph:
    # The graph is stored in an adjacency dictionary where each key 
    # represents a node in the graph and each value in the dictionary
    # represents the corresponding key's list of edges
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict

    # Breadth first search of a graph, iterative 
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
                for neighbor in self.adjacency_dict[current]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)


        return visited

    # Depth first search of a graph, iterative
    def depth_first_search(self):
        graph = self.adjacency_dict
        stack = []
        visited = []

        if self.adjacency_dict:
            first_node = list(graph.keys())[0]
            stack.append(first_node)
        
        while stack:
            current = stack.pop(-1)
            visited.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return visited 

    # Depth first search of a graph, recursive
    def depth_first_search_recursive_helper(self, graph, node, visited):
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                self.depth_first_search_recursive_helper(graph, neighbor, visited)

        

    def depth_first_search_recursive(self):
        visited = []

        if self.adjacency_dict:
            first_node = list(self.adjacency_dict.keys())[0]
            self.depth_first_search_recursive_helper(self.adjacency_dict, first_node, visited)
        
        return visited 

