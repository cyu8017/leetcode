# LeetCode 2081 - Sum of k-Mirror Numbers
# https://leetcode.com/problems/sum-of-k-mirror-numbers/


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_pal_base(x: int, bas: int) -> bool:
            digits = []
            while x > 0:
                digits.append(x % bas)
                x //= bas
            l, r = 0, len(digits) - 1
            while l < r:
                if digits[l] != digits[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 0
        count = 0
        length = 1
        while count < n:
            start = 1
            for _ in range((length + 1) // 2 - 1):
                start *= 10
            end = start * 10
            half = start
            while half < end and count < n:
                pal = half
                if length % 2 == 0:
                    x = half
                    while x > 0:
                        pal = pal * 10 + x % 10
                        x //= 10
                else:
                    x = half // 10
                    while x > 0:
                        pal = pal * 10 + x % 10
                        x //= 10
                if is_pal_base(pal, k):
                    ans += pal
                    count += 1
                half += 1
            length += 1
        return ans
