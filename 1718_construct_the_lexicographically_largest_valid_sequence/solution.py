from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(i: int) -> bool:
            while i < len(ans) and ans[i]:
                i += 1
            if i == len(ans):
                return True
            for value in range(n, 0, -1):
                if used[value]:
                    continue
                if value == 1:
                    ans[i] = 1
                    used[1] = True
                    if backtrack(i + 1):
                        return True
                    used[1] = False
                    ans[i] = 0
                else:
                    j = i + value
                    if j < len(ans) and ans[j] == 0:
                        ans[i] = ans[j] = value
                        used[value] = True
                        if backtrack(i + 1):
                            return True
                        used[value] = False
                        ans[i] = ans[j] = 0
            return False

        backtrack(0)
        return ans
