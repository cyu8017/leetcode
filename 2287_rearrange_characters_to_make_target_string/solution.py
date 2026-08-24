# LeetCode 2287 - Rearrange Characters to Make Target String
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = [0] * 26
        tc = [0] * 26
        for c in s:
            sc[ord(c) - 97] += 1
        for c in target:
            tc[ord(c) - 97] += 1
        ans = float("inf")
        for i in range(26):
            if tc[i] == 0:
                continue
            ans = min(ans, sc[i] // tc[i])
        return int(ans)
