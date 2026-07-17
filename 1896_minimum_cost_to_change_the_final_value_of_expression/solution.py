# LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def combine(left: list[int], op: str, right: list[int]) -> list[int]:
            left_val, left_to_zero, left_to_one = left
            right_val, right_to_zero, right_to_one = right
            if op == "&":
                and_val = left_val & right_val
                and_to_zero = min(left_to_zero, left_to_one + right_to_zero)
                and_to_one = left_to_one + right_to_one
                or_to_zero = left_to_zero + right_to_zero
                or_to_one = min(left_to_one, left_to_zero + right_to_one, right_to_zero + left_to_one)
                val = and_val
                to_zero = min(and_to_zero, 1 + or_to_zero)
                to_one = min(and_to_one, 1 + or_to_one)
            else:
                or_val = left_val | right_val
                or_to_zero = left_to_zero + right_to_zero
                or_to_one = min(left_to_one, left_to_zero + right_to_one, right_to_zero + left_to_one)
                and_to_zero = min(left_to_zero, left_to_one + right_to_zero)
                and_to_one = left_to_one + right_to_one
                val = or_val
                to_zero = min(or_to_zero, 1 + and_to_zero)
                to_one = min(or_to_one, 1 + and_to_one)
            return [val, to_zero, to_one]

        index = 0

        def parse_expr() -> list[int]:
            nonlocal index
            node = parse_factor()
            while index < len(expression) and expression[index] in "&|":
                op = expression[index]
                index += 1
                node = combine(node, op, parse_factor())
            return node

        def parse_factor() -> list[int]:
            nonlocal index
            if expression[index] in "01":
                value = int(expression[index])
                index += 1
                to_zero = 0 if value == 0 else 1
                to_one = 1 if value == 0 else 0
                return [value, to_zero, to_one]
            index += 1
            node = parse_expr()
            index += 1
            return node

        value, to_zero, to_one = parse_expr()
        return to_zero if value else to_one
