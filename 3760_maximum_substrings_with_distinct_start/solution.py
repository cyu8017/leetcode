# LeetCode 3760 - Maximum Substrings with Distinct Start
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution:
    def maxDistinct(self, s: str) -> int:
        cnt = [0] * 26
        ans = 0
        for c in s:
            i = ord(c) - 97
            cnt[i] += 1
            if cnt[i] == 1:
                ans += 1
        return ans
