# LeetCode 2953 - Count Complete Substrings
# https://leetcode.com/problems/count-complete-substrings/


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j + 1 < n and abs(ord(word[j + 1]) - ord(word[j])) <= 2:
                j += 1
            seg = word[i : j + 1]
            m = len(seg)
            for chars in range(1, 27):
                length = chars * k
                if length > m:
                    break
                freq = [0] * 26
                unique = 0
                for r in range(m):
                    c = ord(seg[r]) - 97
                    freq[c] += 1
                    if freq[c] == 1:
                        unique += 1
                    if r >= length:
                        c2 = ord(seg[r - length]) - 97
                        freq[c2] -= 1
                        if freq[c2] == 0:
                            unique -= 1
                    if r >= length - 1 and unique == chars:
                        ok = True
                        for f in freq:
                            if f != 0 and f != k:
                                ok = False
                                break
                        if ok:
                            ans += 1
            i = j + 1
        return ans
