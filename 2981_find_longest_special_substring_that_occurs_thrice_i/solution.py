# LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        ans = -1
        for i in range(n):
            for j in range(i, n):
                if s[j] != s[i]:
                    break
                length = j - i + 1
                cnt = 0
                for k in range(0, n - length + 1):
                    ok = True
                    for t in range(length):
                        if s[k + t] != s[i + t]:
                            ok = False
                            break
                    if ok:
                        cnt += 1
                if cnt >= 3 and length > ans:
                    ans = length
        return ans
