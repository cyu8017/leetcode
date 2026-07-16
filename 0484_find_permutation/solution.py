# LeetCode 0484 - Find Permutation
# https://leetcode.com/problems/find-permutation/

class Solution:
    def findPermutation(self, s: str) -> list[int]:
        stack = [1]
        result: list[int] = []
        for ch in s:
            if ch == "I":
                while stack:
                    result.append(stack.pop())
            stack.append(len(stack) + len(result) + 1)
        while stack:
            result.append(stack.pop())
        return result
