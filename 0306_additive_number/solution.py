# LeetCode 0306 - Additive Number
# https://leetcode.com/problems/additive-number/


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def valid(first: str, second: str, start: int) -> bool:
            if (len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0"):
                return False
            while start < len(num):
                total = str(int(first) + int(second))
                if not num.startswith(total, start):
                    return False
                first, second = second, total
                start += len(total)
            return True

        for first_end in range(1, len(num)):
            for second_end in range(first_end + 1, len(num)):
                if valid(num[:first_end], num[first_end:second_end], second_end):
                    return True
        return False
