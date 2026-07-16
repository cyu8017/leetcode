# LeetCode 0491 - Non-decreasing Subsequences
# https://leetcode.com/problems/non-decreasing-subsequences/

class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        result: set[tuple[int, ...]] = set()

        def backtrack(start: int, path: list[int]) -> None:
            if len(path) >= 2:
                result.add(tuple(path))
            used: set[int] = set()
            for index in range(start, len(nums)):
                if nums[index] in used:
                    continue
                if path and nums[index] < path[-1]:
                    continue
                used.add(nums[index])
                path.append(nums[index])
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return [list(item) for item in sorted(result)]
