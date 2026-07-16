# LeetCode 1036 - Escape a Large Maze
# https://leetcode.com/problems/escape-a-large-maze/

from collections import deque


class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        blocked_set = {tuple(b) for b in blocked}
        # Max area enclosable by B blocked cells against the border is B*(B-1)/2.
        limit = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start: list[int], goal: list[int]) -> bool:
            queue = deque([tuple(start)])
            seen = {tuple(start)}
            while queue:
                if len(seen) > limit:
                    return True
                r, c = queue.popleft()
                if [r, c] == goal:
                    return True
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < 10**6 and 0 <= nc < 10**6 and (nr, nc) not in blocked_set and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            return False

        return bfs(source, target) and bfs(target, source)
