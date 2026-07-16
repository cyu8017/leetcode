# LeetCode 0564 - Find the Closest Palindrome
# https://leetcode.com/problems/find-the-closest-palindrome/


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        number = int(n)
        candidates: set[int] = {
            10 ** (length - 1) - 1,
            10**length + 1,
        }

        prefix = int(n[: (length + 1) // 2])
        for half in (prefix - 1, prefix, prefix + 1):
            text = str(half)
            if length % 2 == 0:
                palindrome = text + text[::-1]
            else:
                palindrome = text + text[-2::-1]
            candidates.add(int(palindrome))

        candidates.discard(number)
        best = min(candidates, key=lambda value: (abs(value - number), value))
        return str(best)
