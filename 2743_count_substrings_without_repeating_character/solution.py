# LeetCode 2743 - Count Substrings Without Repeating Character
# https://leetcode.com/problems/count-substrings-without-repeating-character/


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        n = len(s)
        ans, left = 0, 0
        cnt = [0] * 26
        for i in range(n):
            c = ord(s[i]) - 97
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[ord(s[left]) - 97] -= 1
                left += 1
            ans += i - left + 1
        return ans
