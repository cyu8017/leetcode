# LeetCode 2729 - Check if The Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/


class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        if len(s) != 9:
            return False
        cnt = [0] * 10
        for c in s:
            cnt[ord(c) - 48] += 1
        if cnt[0] != 0:
            return False
        for i in range(1, 10):
            if cnt[i] != 1:
                return False
        return True
