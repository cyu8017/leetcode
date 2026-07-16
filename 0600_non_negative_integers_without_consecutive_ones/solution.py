# LeetCode 0600 - Non-negative Integers without Consecutive Ones
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/


class Solution:
    def findIntegers(self, n: int) -> int:
        # fib[i] = count of valid i-bit strings (including leading zeros)
        fib = [0] * 32
        fib[0], fib[1] = 1, 2
        for i in range(2, 32):
            fib[i] = fib[i - 1] + fib[i - 2]

        answer = 0
        prev_bit = 0
        for bit in range(30, -1, -1):
            if n & (1 << bit):
                answer += fib[bit]
                if prev_bit == 1:
                    return answer
                prev_bit = 1
            else:
                prev_bit = 0

        return answer + 1
