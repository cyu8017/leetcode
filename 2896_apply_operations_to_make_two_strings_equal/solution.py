# LeetCode 2896 - Apply Operations to Make Two Strings Equal
# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        m = len(diff)
        if m % 2 == 1:
            return -1
        if m == 0:
            return 0
        inf = 1 << 30
        dp2 = [inf] * (m + 1)
        dp2[0] = 0
        for i in range(m):
            if dp2[i] >= inf:
                continue
            if i + 1 < m:
                cand = diff[i + 1] - diff[i]
                if cand > x:
                    cand = x
                if dp2[i] + cand < dp2[i + 2]:
                    dp2[i + 2] = dp2[i] + cand
        return -1 if dp2[m] >= inf else dp2[m]
