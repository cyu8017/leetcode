# LeetCode 3581 - Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/


class Solution:
    def countOddLetters(self, n: int) -> int:
        d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        mask = 0
        while n > 0:
            for c in d[n % 10]:
                mask ^= 1 << (ord(c) - 97)
            n //= 10
        cnt = 0
        while mask:
            cnt += mask & 1
            mask >>= 1
        return cnt
