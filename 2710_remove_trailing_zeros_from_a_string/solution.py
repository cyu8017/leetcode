# LeetCode 2710 - Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        end = len(num)
        while end > 0 and num[end - 1] == "0":
            end -= 1
        return num[:end]
