# LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        ans = [1] * n
        one = -1
        for i, v in enumerate(nums):
            if v == 1:
                one = i
                break
        if one < 0:
            return ans
        seen = set()

        def collect(u: int) -> None:
            if nums[u] in seen:
                return
            seen.add(nums[u])
            for v in children[u]:
                collect(v)

        miss, node, prev = 1, one, -1
        while node != -1:
            for v in children[node]:
                if v != prev:
                    collect(v)
            seen.add(nums[node])
            while miss in seen:
                miss += 1
            ans[node] = miss
            prev = node
            node = parents[node]
        return ans
