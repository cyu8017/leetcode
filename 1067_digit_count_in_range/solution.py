# LeetCode 1067 - Digit Count in Range
# https://leetcode.com/problems/digit-count-in-range/

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count_upto(n: int) -> int:
            if n < 0:
                return 0
            s = str(n)
            length = len(s)
            ans = 0
            for i in range(length):
                left = int(s[:i]) if i else 0
                right = int(s[i + 1 :]) if i + 1 < length else 0
                digit = int(s[i])
                power = 10 ** (length - i - 1)
                if d != 0:
                    ans += left * power
                    if digit > d:
                        ans += power
                    elif digit == d:
                        ans += right + 1
                else:
                    if i == 0:
                        continue
                    ans += (left - 1) * power
                    if digit > 0:
                        ans += power
                    else:
                        ans += right + 1
            return ans

        return count_upto(high) - count_upto(low - 1)
