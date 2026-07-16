# LeetCode 0749 - Contain Virus
# https://leetcode.com/problems/contain-virus/

from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        def neighbors(r: int, c: int):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        while True:
            seen: set[tuple[int, int]] = set()
            regions: list[set[tuple[int, int]]] = []
            frontiers: list[set[tuple[int, int]]] = []
            perimeters: list[int] = []

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in seen:
                        stack = [(i, j)]
                        seen.add((i, j))
                        region: set[tuple[int, int]] = set()
                        frontier: set[tuple[int, int]] = set()
                        perimeter = 0
                        while stack:
                            r, c = stack.pop()
                            region.add((r, c))
                            for nr, nc in neighbors(r, c):
                                if isInfected[nr][nc] == 1 and (nr, nc) not in seen:
                                    seen.add((nr, nc))
                                    stack.append((nr, nc))
                                elif isInfected[nr][nc] == 0:
                                    frontier.add((nr, nc))
                                    perimeter += 1
                        regions.append(region)
                        frontiers.append(frontier)
                        perimeters.append(perimeter)

            if not regions:
                break

            quarantine = max(range(len(regions)), key=lambda i: len(frontiers[i]))
            if not frontiers[quarantine]:
                break

            walls += perimeters[quarantine]
            for r, c in regions[quarantine]:
                isInfected[r][c] = -1

            for index, frontier in enumerate(frontiers):
                if index == quarantine:
                    continue
                for r, c in frontier:
                    isInfected[r][c] = 1

        return walls
