from collections import defaultdict

class GraphDFS:
    def __init__(self):
        # Initialize an empty adjacency list using defaultdict
        self.adjacency_list = defaultdict(list)

    def add_edge(self, source, destination):
        # Add the edge in both directions (undirected graph)
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def depth_first_search(self, start_node):
        # Create a set to track visited nodes
        visited = set()
        # Start DFS traversal from the given node
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, node, visited):
        # If the node is already visited, return
        if node in visited:
            return

        # Print the node (processing step)
        print(node, end=" ")
        # Mark the node as visited
        visited.add(node)

        # Recursively visit all the neighbors
        for neighbor in self.adjacency_list.get(node, []):
            self._dfs_recursive(neighbor, visited)

# Driver code
if __name__ == "__main__":
    graph = GraphDFS()

    # Add edges to the graph
    graph.add_edge('a', 'b')
    graph.add_edge('a', 'h')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'h')
    graph.add_edge('c', 'd')
    graph.add_edge('c', 'i')
    graph.add_edge('c', 'f')
    graph.add_edge('d', 'e')
    graph.add_edge('d', 'f')
    graph.add_edge('e', 'f')
    graph.add_edge('f', 'g')
    graph.add_edge('g', 'h')
    graph.add_edge('g', 'i')
    graph.add_edge('h', 'i')

    # Perform DFS starting from node 'a'
    print("Depth First Search starting from node 'a':")
    graph.depth_first_search('a')

