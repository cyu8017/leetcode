# LeetCode 2726 - Calculator with Method Chaining
# https://leetcode.com/problems/calculator-with-method-chaining/


class Calculator:
    def __init__(self, value: float):
        self.val = value

    def add(self, value: float) -> "Calculator":
        self.val += value
        return self

    def subtract(self, value: float) -> "Calculator":
        self.val -= value
        return self

    def multiply(self, value: float) -> "Calculator":
        self.val *= value
        return self

    def divide(self, value: float) -> "Calculator":
        if value == 0:
            raise Exception("Division by zero is not allowed")
        self.val /= value
        return self

    def power(self, value: float) -> "Calculator":
        self.val = self.val ** value
        return self

    def getResult(self) -> float:
        return self.val


class Solution:
    def Calculator(self, value: float) -> Calculator:
        return Calculator(value)
