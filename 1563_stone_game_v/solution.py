from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = [0]
        for x in stoneValue:
            pre.append(pre[-1] + x)
        dp = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        for i, x in enumerate(stoneValue):
            left[i][i] = right[i][i] = x
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                lo, hi = i, j - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                split = lo
                left_sum = pre[split + 1] - pre[i]
                right_sum = pre[j + 1] - pre[split + 1]
                best = right[split + 1][j]
                if left_sum == right_sum:
                    best = max(best, left[i][split])
                elif split > i:
                    best = max(best, left[i][split - 1])
                dp[i][j] = best
                total = pre[j + 1] - pre[i]
                left[i][j] = max(left[i][j - 1], total + best)
                right[i][j] = max(right[i + 1][j], total + best)
        return dp[0][n - 1] if n else 0
