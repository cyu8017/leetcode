# LeetCode 1101 - The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True

        logs.sort()
        components = n
        for t, a, b in logs:
            if union(a, b):
                components -= 1
                if components == 1:
                    return t
        return -1
