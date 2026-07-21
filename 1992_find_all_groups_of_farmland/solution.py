from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans: List[List[int]] = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    r, c = i, j
                    while r + 1 < m and land[r + 1][j] == 1:
                        r += 1
                    while c + 1 < n and land[i][c + 1] == 1:
                        c += 1
                    ans.append([i, j, r, c])
        return ans
