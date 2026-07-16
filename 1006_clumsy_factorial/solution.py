# LeetCode 1006 - Clumsy Factorial
# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        op = 0
        while n:
            if op % 4 == 0:
                stack.append(stack.pop() * n)
            elif op % 4 == 1:
                stack.append(int(stack.pop() / n))
            elif op % 4 == 2:
                stack.append(n)
            else:
                stack.append(-n)
            n -= 1
            op += 1
        return sum(stack)
