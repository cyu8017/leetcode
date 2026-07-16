# LeetCode 0470 - Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/


def rand7() -> int:
    raise RuntimeError("rand7 must be provided by the test harness")


class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return (num - 1) % 10 + 1
