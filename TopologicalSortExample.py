from collections import defaultdict

class TopologicalSortExample:
    def __init__(self, vertices):
        # Initialize number of vertices and adjacency list
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    # Function to add a directed edge from src to dest
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

    # Function to perform Topological Sort using DFS
    def topological_sort(self):
        visited = [False] * self.vertices  # Track visited vertices
        stack = []  # Stack to store the topological sort order

        # Perform DFS for all unvisited nodes
        for v in range(self.vertices):
            if not visited[v]:
                self.dfs(v, visited, stack)

        # Print topological order by converting index to characters starting from 'm'
        print("Topological Sort Order:")
        while stack:
            print(chr(stack.pop() + ord('m')), end=" ")  # Convert index to char
        print()

    # Helper function for DFS
    def dfs(self, v, visited, stack):
        visited[v] = True  # Mark the current node as visited

        # Recur for all the adjacent vertices
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(v)  # Push current node to stack after visiting neighbors

# ---------------------- Main Part ----------------------
if __name__ == "__main__":
    # Create a graph with 12 nodes representing characters m to x
    graph = TopologicalSortExample(12)

    # Add edges (converted from character to index: 'm' is 0, 'n' is 1, ..., 'x' is 11)
    graph.add_edge(0, 4)   # m -> q
    graph.add_edge(0, 5)   # m -> r
    graph.add_edge(0, 9)   # m -> v
    graph.add_edge(1, 4)   # n -> q
    graph.add_edge(1, 6)   # n -> s
    graph.add_edge(1, 2)   # n -> o
    graph.add_edge(2, 5)   # o -> r
    graph.add_edge(2, 7)   # o -> t
    graph.add_edge(2, 10)  # o -> w
    graph.add_edge(3, 2)   # p -> o
    graph.add_edge(3, 7)   # p -> t
    graph.add_edge(3, 11)  # p -> x
    graph.add_edge(4, 8)   # q -> u
    graph.add_edge(5, 6)   # r -> s
    graph.add_edge(5, 10)  # r -> w
    graph.add_edge(7, 5)   # t -> r
    graph.add_edge(8, 9)   # u -> v
    graph.add_edge(8, 10)  # u -> w
    graph.add_edge(6, 10)  # s -> w
    graph.add_edge(10, 11) # w -> x
    graph.add_edge(9, 11)  # v -> x

    # Perform topological sort and display the result
    graph.topological_sort()

