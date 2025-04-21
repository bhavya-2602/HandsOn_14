class Edge:
    def __init__(self, source, destination, weight):
        # Initialize an edge with source, destination, and weight
        self.source = source
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        # Allows sorting edges by weight
        return self.weight < other.weight


class KruskalAlgorithm:
    def __init__(self):
        self.edges = []        # List to store all edges
        self.parent = {}       # Parent map for disjoint set
        self.rank = {}         # Rank map for union by rank

    def add_edge(self, source, destination, weight):
        # Add an edge to the graph
        self.edges.append(Edge(source, destination, weight))

        # Initialize disjoint set parent and rank
        if source not in self.parent:
            self.parent[source] = source
            self.rank[source] = 0
        if destination not in self.parent:
            self.parent[destination] = destination
            self.rank[destination] = 0

    def find_parent(self, node):
        # Find the root of the node with path compression
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Union two sets using rank
        root1 = self.find_parent(node1)
        root2 = self.find_parent(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

    def kruskal_mst(self):
        # Sort all edges by weight
        self.edges.sort()

        mst = []             # List to store MST edges
        total_weight = 0     # Total weight of MST

        for edge in self.edges:
            # If edge doesn't form a cycle, add it to MST
            if self.find_parent(edge.source) != self.find_parent(edge.destination):
                mst.append(edge)
                total_weight += edge.weight
                self.union(edge.source, edge.destination)

        # Display MST result
        print("Edges in the Minimum Spanning Tree (MST):")
        for edge in mst:
            print(f"{edge.source} - {edge.destination} : {edge.weight}")
        print(f"Total weight of MST: {total_weight}")


# Driver code
if __name__ == "__main__":
    graph = KruskalAlgorithm()

    # Add all edges to the graph
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'h', 8)
    graph.add_edge('b', 'h', 11)
    graph.add_edge('b', 'c', 8)
    graph.add_edge('c', 'i', 2)
    graph.add_edge('c', 'f', 4)
    graph.add_edge('c', 'd', 7)
    graph.add_edge('d', 'e', 9)
    graph.add_edge('d', 'f', 14)
    graph.add_edge('e', 'f', 10)
    graph.add_edge('f', 'g', 2)
    graph.add_edge('g', 'h', 1)
    graph.add_edge('g', 'i', 6)
    graph.add_edge('h', 'i', 7)

    # Run Kruskal's algorithm to find MST
    graph.kruskal_mst()

