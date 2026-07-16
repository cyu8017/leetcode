# LeetCode 0666 - Path Sum IV
# https://leetcode.com/problems/path-sum-iv/

from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for num in nums:
            depth, pos, val = num // 100, (num // 10) % 10, num % 10
            tree[(depth, pos)] = val

        total = 0

        def dfs(depth: int, pos: int, path: int) -> None:
            nonlocal total
            if (depth, pos) not in tree:
                return
            path += tree[(depth, pos)]
            left = (depth + 1, pos * 2 - 1)
            right = (depth + 1, pos * 2)
            if left not in tree and right not in tree:
                total += path
                return
            dfs(depth + 1, pos * 2 - 1, path)
            dfs(depth + 1, pos * 2, path)

        dfs(1, 1, 0)
        return total
