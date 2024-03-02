class MazeSolverDFS:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = set()

    def solve_maze(self, start, end):
        self.visited.clear()
        path = []
        if self.dfs(start, end, path):
            return path
        else:
            return None

    def dfs(self, curr, end, path):
        if curr == end:
            path.append(curr)
            return True

        self.visited.add(curr)
        path.append(curr)

        row, col = curr
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if (new_row, new_col) not in self.visited:
                    if self.maze[new_row][new_col] == 1:
                        if self.dfs((new_row, new_col), end, path):
                            return True

        path.pop()
        return False

# Example usage with provided maze
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solver = MazeSolverDFS(maze)
start = (3, 11)
end = (10, 0)
path = solver.solve_maze(start, end)

if path:
    print("Path found:")
    for k, position in enumerate(path):
        print(k+1, position)
else:
    print("No path found.")
    