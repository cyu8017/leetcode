# LeetCode 2751 - Robot Collisions
# https://leetcode.com/problems/robot-collisions/

from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        idx = list(range(n))
        idx.sort(key=lambda i: positions[i])
        stack = []
        for i in idx:
            cur = [i, healths[i], directions[i]]
            while stack and stack[-1][2] == "R" and cur[2] == "L":
                top = stack[-1]
                if top[1] == cur[1]:
                    stack.pop()
                    cur[1] = 0
                    break
                if top[1] > cur[1]:
                    top[1] -= 1
                    cur[1] = 0
                    break
                cur[1] -= 1
                stack.pop()
            if cur[1] > 0:
                stack.append(cur)
        alive = {i: h for i, h, _ in stack}
        return [alive[i] for i in range(n) if i in alive]
