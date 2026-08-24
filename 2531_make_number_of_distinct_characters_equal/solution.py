# LeetCode 2531 - Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        for c in word1:
            c1[ord(c) - 97] += 1
        for c in word2:
            c2[ord(c) - 97] += 1
        d1 = d2 = 0
        for i in range(26):
            if c1[i] > 0:
                d1 += 1
            if c2[i] > 0:
                d2 += 1
        for a in range(26):
            if c1[a] == 0:
                continue
            for b in range(26):
                if c2[b] == 0:
                    continue
                nd1, nd2 = d1, d2
                if a == b:
                    if nd1 == nd2:
                        return True
                    continue
                if c1[a] == 1:
                    nd1 -= 1
                if c1[b] == 0:
                    nd1 += 1
                if c2[b] == 1:
                    nd2 -= 1
                if c2[a] == 0:
                    nd2 += 1
                if nd1 == nd2:
                    return True
        return False
