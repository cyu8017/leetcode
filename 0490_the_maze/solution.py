# LeetCode 0490 - The Maze
# https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int],
    ) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited: set[tuple[int, int]] = set()
        stack = [(start[0], start[1])]

        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if [row, col] == destination:
                return True
            for dr, dc in directions:
                nr, nc = row, col
                while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    stack.append((nr, nc))
        return False
