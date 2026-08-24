# LeetCode 3821 - Find Nth Smallest Integer with K One Bits
# https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        MX = 50
        C = [[0] * (MX + 1) for _ in range(MX)]
        for i in range(MX):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
        ans = 0
        nn = n
        for i in range(49, -1, -1):
            if k >= 0 and nn > C[i][k]:
                nn -= C[i][k]
                ans |= 1 << i
                k -= 1
                if k == 0:
                    break
        return ans
