# LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        odd = 0
        mid = -1
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd += 1
                mid = i
        if odd > 1:
            return ""
        half = [cnt[i] // 2 for i in range(26)]
        n = len(s)
        half_len = n // 2
        left = [""] * half_len

        def dfs(pos: int, greater: bool) -> bool:
            if pos == half_len:
                if mid >= 0:
                    if greater:
                        return True
                    return chr(97 + mid) > target[half_len]
                return greater
            start = 0 if greater else (ord(target[pos]) - 97)
            for c in range(start, 26):
                if half[c] == 0:
                    continue
                half[c] -= 1
                left[pos] = chr(97 + c)
                if dfs(pos + 1, greater or c > (ord(target[pos]) - 97)):
                    return True
                half[c] += 1
            return False

        if not dfs(0, False):
            return ""
        res = "".join(left)
        if mid >= 0:
            res += chr(97 + mid)
        for i in range(half_len - 1, -1, -1):
            res += left[i]
        if res <= target:
            return ""
        return res
