# LeetCode 0537 - Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num: str) -> tuple[int, int]:
            real, imag = num.split("+")
            return int(real), int(imag[:-1])

        a, b = parse(num1)
        c, d = parse(num2)
        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"
