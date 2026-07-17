# LeetCode 1849 - Splitting a String Into Descending Consecutive Values
# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(index: int, previous: int | None, parts: int) -> bool:
            if index == n:
                return parts >= 2

            for end in range(index + 1, n + 1):
                value = int(s[index:end])
                if previous is None:
                    if dfs(end, value, parts + 1):
                        return True
                elif value == previous - 1:
                    if dfs(end, value, parts + 1):
                        return True
                elif value > previous - 1:
                    break

            return False

        return dfs(0, None, 0)
