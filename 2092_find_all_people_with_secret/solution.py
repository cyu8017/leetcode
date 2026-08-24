# LeetCode 2092 - Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/

from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda m: m[2])
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b

        know = [False] * n
        know[0] = know[firstPerson] = True
        unite(0, firstPerson)
        i = 0
        while i < len(meetings):
            j = i
            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                j += 1
            for k in range(i, j):
                unite(meetings[k][0], meetings[k][1])
            root0 = find(0)
            reset = []
            for k in range(i, j):
                a, b = meetings[k][0], meetings[k][1]
                if find(a) != root0:
                    reset.append(a)
                    reset.append(b)
                else:
                    know[a] = know[b] = True
            for x in reset:
                parent[x] = x
            i = j
        return [i for i in range(n) if find(i) == find(0) or know[i]]
