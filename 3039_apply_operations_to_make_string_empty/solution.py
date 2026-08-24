# LeetCode 3039 - Apply Operations to Make String Empty
# https://leetcode.com/problems/apply-operations-to-make-string-empty/


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = [0] * 26
        last = [0] * 26
        mx = 0
        for i in range(len(s)):
            c = ord(s[i]) - 97
            cnt[c] += 1
            last[c] = i
            mx = max(mx, cnt[c])
        ans = ""
        for i in range(len(s)):
            c = ord(s[i]) - 97
            if cnt[c] == mx and last[c] == i:
                ans += s[i]
        return ans
