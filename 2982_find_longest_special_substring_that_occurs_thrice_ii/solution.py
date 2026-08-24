# LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/


class Solution:
    def maximumLength(self, s: str) -> int:
        groups = [[] for _ in range(26)]
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            groups[ord(s[i]) - 97].append(j - i)
            i = j
        ans = -1
        for c in range(26):
            arr = groups[c]
            if not arr:
                continue
            arr.sort(reverse=True)
            for L in range(arr[0], 0, -1):
                cnt = 0
                for g in arr:
                    if g >= L:
                        cnt += g - L + 1
                if cnt >= 3:
                    if L > ans:
                        ans = L
                    break
        return ans
