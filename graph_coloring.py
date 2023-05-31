class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.solution = {}

    def solve(self):
        if self._backtrack():
            self._print_solution()
        else:
            print("No solution found.")

    def _backtrack(self, node=0):
        if node == len(self.graph):
            return True

        for color in self.colors:
            if self._is_safe(node, color):
                self.solution[node] = color

                if self._backtrack(node + 1):
                    return True

                del self.solution[node]

        return False

    def _is_safe(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.solution and self.solution[neighbor] == color:
                return False

        return True

    def _print_solution(self):
        for node, color in self.solution.items():
            print(f"Node {node}: Color {color}")


# Example usage
if __name__ == '__main__':
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    # Define the available colors
    colors = ['Red', 'Green', 'Blue']

    # Create a GraphColoring object
    problem = GraphColoring(graph, colors)

    # Solve the graph coloring problem
    problem.solve()
