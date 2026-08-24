# LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

from typing import List
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * (n)
        depth = [1] * (n)
        for f in favorite:
            indeg[f] += 1
        q = []
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.pop(0)
            v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        pairSum = 0
        maxCycle = 0
        vis = [False] * (n)
        for i in range(n):
            if indeg[i] == 0 or vis[i]:
                continue
            u = i
            lenCycle = 0
            while not vis[u]:
                vis[u] = True
                u = favorite[u]
                lenCycle += 1
            if lenCycle == 2:
                pairSum += depth[i] + depth[favorite[i]]
            else:
                maxCycle = max(maxCycle, lenCycle)
        return max(pairSum, maxCycle)
