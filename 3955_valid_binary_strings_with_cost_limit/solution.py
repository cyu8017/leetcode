# LeetCode 3955 - Valid Binary Strings With Cost Limit
# https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

from typing import List


class Solution:
    def generateValidStrings(self, n: int, k: int) -> List[str]:
        ans: List[str] = []
        path: List[str] = []
        self.dfs(0, 0, n, k, path, ans)
        return ans

    def dfs(self, i: int, tot: int, n: int, k: int, path: List[str], ans: List[str]) -> None:
        if i >= n:
            ans.append("".join(path))
            return
        path.append("0")
        self.dfs(i + 1, tot, n, k, path, ans)
        path.pop()
        if (len(path) == 0 or path[-1] == "0") and tot + i <= k:
            path.append("1")
            self.dfs(i + 1, tot + i, n, k, path, ans)
            path.pop()
