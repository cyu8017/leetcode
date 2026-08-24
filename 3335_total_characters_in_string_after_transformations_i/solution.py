# LeetCode 3335 - Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1000000007
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        for _ in range(t):
            ncnt = [0] * 26
            for i in range(25):
                ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod
            ncnt[0] = (ncnt[0] + cnt[25]) % mod
            ncnt[1] = (ncnt[1] + cnt[25]) % mod
            cnt = ncnt
        ans = 0
        for v in cnt:
            ans = (ans + v) % mod
        return ans
