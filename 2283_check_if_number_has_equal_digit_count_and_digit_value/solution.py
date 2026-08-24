# LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/


class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = [0] * 10
        for c in num:
            cnt[ord(c) - 48] += 1
        for i in range(len(num)):
            if cnt[i] != ord(num[i]) - 48:
                return False
        return True
