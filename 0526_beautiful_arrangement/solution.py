# LeetCode 0526 - Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0

        def backtrack(index: int, used: set[int]) -> None:
            nonlocal count
            if index == n + 1:
                count += 1
                return
            for num in range(1, n + 1):
                if num in used:
                    continue
                if index % num == 0 or num % index == 0:
                    used.add(num)
                    backtrack(index + 1, used)
                    used.remove(num)

        backtrack(1, set())
        return count
