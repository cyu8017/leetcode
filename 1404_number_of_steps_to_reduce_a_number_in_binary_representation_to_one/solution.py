class Solution:
    def numSteps(self, s):
        steps = carry = 0
        for bit in reversed(s[1:]):
            value = int(bit) + carry
            if value == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
