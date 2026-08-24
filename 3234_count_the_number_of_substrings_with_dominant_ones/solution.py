# LeetCode 3234 - Count the Number of Substrings With Dominant Ones
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        nxt = [0] * (n + 1)
        nxt[n] = n
        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1]
            if s[i] == "0":
                nxt[i] = i
        ans = 0
        for i in range(n):
            cnt0 = 1 if s[i] == "0" else 0
            j = i
            while j < n and cnt0 * cnt0 <= n:
                cnt1 = nxt[j + 1] - i - cnt0
                if cnt1 >= cnt0 * cnt0:
                    ans += min(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1)
                j = nxt[j + 1]
                cnt0 += 1
        return ans
