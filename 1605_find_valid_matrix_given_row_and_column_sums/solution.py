class Solution:
    def restoreMatrix(self, rowSum, colSum):
        ans = [[0] * len(colSum) for _ in rowSum]
        i = j = 0
        while i < len(rowSum) and j < len(colSum):
            x = min(rowSum[i], colSum[j]); ans[i][j] = x
            rowSum[i] -= x; colSum[j] -= x
            if rowSum[i] == 0: i += 1
            if colSum[j] == 0: j += 1
        return ans
