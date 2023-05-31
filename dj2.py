import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def dijkstra(self, src):
        distance = [sys.maxsize] * self.vertices
        distance[src] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            min_dist = sys.maxsize
            min_index = -1

            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_index = v

            visited[min_index] = True

            for v in range(self.vertices):
                if (
                    not visited[v]
                    and self.graph[min_index][v] != 0
                    and distance[min_index] + self.graph[min_index][v] < distance[v]
                ):
                    distance[v] = distance[min_index] + self.graph[min_index][v]

        self.print_solution(distance)

    def print_solution(self, distance):
        print("Vertex \tDistance from Source")
        for v in range(self.vertices):
            print(f"{v} \t\t{distance[v]}")


# Example usage
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 3, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 4)
 
    graph.dijkstra(0)
