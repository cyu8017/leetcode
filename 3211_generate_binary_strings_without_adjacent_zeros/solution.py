# LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans: List[str] = []
        t: List[str] = []

        def dfs(i: int) -> None:
            if i >= n:
                ans.append("".join(t))
                return
            for j in range(2):
                if (j == 0 and (i == 0 or t[i - 1] == "1")) or j == 1:
                    t.append(str(j))
                    dfs(i + 1)
                    t.pop()

        dfs(0)
        return ans
