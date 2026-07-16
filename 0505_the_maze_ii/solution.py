# LeetCode 0505 - The Maze II
# https://leetcode.com/problems/the-maze-ii/

import heapq


class Solution:
    def shortestDistance(
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int],
    ) -> int:
        rows, cols = len(maze), len(maze[0])
        target = (destination[0], destination[1])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        best: dict[tuple[int, int], int] = {}
        heap: list[tuple[int, int, int]] = [(0, start[0], start[1])]

        while heap:
            dist, row, col = heapq.heappop(heap)
            if (row, col) == target:
                return dist
            if best.get((row, col), float("inf")) <= dist:
                continue
            best[(row, col)] = dist
            for dr, dc in directions:
                next_row, next_col = row, col
                traveled = 0
                while 0 <= next_row + dr < rows and 0 <= next_col + dc < cols and maze[next_row + dr][next_col + dc] == 0:
                    next_row += dr
                    next_col += dc
                    traveled += 1
                if (next_row, next_col) != (row, col):
                    new_dist = dist + traveled
                    if new_dist < best.get((next_row, next_col), float("inf")):
                        heapq.heappush(heap, (new_dist, next_row, next_col))
        return -1
