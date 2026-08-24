# LeetCode 2067 - Number of Equal Count Substrings
# https://leetcode.com/problems/number-of-equal-count-substrings/


class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        ans = 0
        n = len(s)
        seen = [False] * 26
        max_unique = 0
        for c in s:
            i = ord(c) - 97
            if not seen[i]:
                seen[i] = True
                max_unique += 1
        for u in range(1, max_unique + 1):
            need_len = u * count
            if need_len > n:
                break
            freq = [0] * 26
            have = 0
            for i in range(n):
                c = ord(s[i]) - 97
                freq[c] += 1
                if freq[c] == count:
                    have += 1
                elif freq[c] == count + 1:
                    have -= 1
                if i >= need_len:
                    p = ord(s[i - need_len]) - 97
                    if freq[p] == count:
                        have -= 1
                    elif freq[p] == count + 1:
                        have += 1
                    freq[p] -= 1
                if i + 1 >= need_len and have == u:
                    ans += 1
        return ans
