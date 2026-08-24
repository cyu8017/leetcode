# LeetCode 3365 - Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        sz = n // k
        cnt = {}
        for i in range(0, n, sz):
            a = s[i : i + sz]
            b = t[i : i + sz]
            cnt[a] = cnt.get(a, 0) + 1
            cnt[b] = cnt.get(b, 0) - 1
        return all(v == 0 for v in cnt.values())
