# LeetCode 0842 - Split Array into Fibonacci Sequence
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        path: list[int] = []

        def dfs(start: int) -> bool:
            if start == n:
                return len(path) >= 3
            for end in range(start, n):
                if num[start] == "0" and end > start:
                    break
                val = int(num[start : end + 1])
                if val > 2**31 - 1:
                    break
                if len(path) >= 2:
                    total = path[-1] + path[-2]
                    if val < total:
                        continue
                    if val > total:
                        break
                path.append(val)
                if dfs(end + 1):
                    return True
                path.pop()
            return False

        dfs(0)
        return path
