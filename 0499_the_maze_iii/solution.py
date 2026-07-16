# LeetCode 0499 - The Maze III
# https://leetcode.com/problems/the-maze-iii/

import heapq


class Solution:
    def findShortestWay(
        self,
        maze: list[list[int]],
        ball: list[int],
        hole: list[int],
    ) -> str:
        rows, cols = len(maze), len(maze[0])
        hole_pos = (hole[0], hole[1])
        directions = {
            "d": (1, 0),
            "l": (0, -1),
            "r": (0, 1),
            "u": (-1, 0),
        }

        def roll(row: int, col: int, dr: int, dc: int) -> tuple[int, int, int]:
            distance = 0
            while 0 <= row + dr < rows and 0 <= col + dc < cols and maze[row + dr][col + dc] == 0:
                row += dr
                col += dc
                distance += 1
                if (row, col) == hole_pos:
                    break
            return row, col, distance

        best: dict[tuple[int, int], tuple[int, str]] = {}
        heap: list[tuple[int, str, int, int]] = [(0, "", ball[0], ball[1])]

        while heap:
            dist, path, row, col = heapq.heappop(heap)
            state = (row, col)
            if state in best and (dist, path) >= best[state]:
                continue
            best[state] = (dist, path)
            if state == hole_pos:
                return path

            for direction, (dr, dc) in directions.items():
                next_row, next_col, traveled = roll(row, col, dr, dc)
                if (next_row, next_col) == (row, col):
                    continue
                new_dist = dist + traveled
                new_path = path + direction
                candidate = (new_dist, new_path)
                target = (next_row, next_col)
                if target not in best or candidate < best[target]:
                    heapq.heappush(heap, (new_dist, new_path, next_row, next_col))

        return "impossible"
