# LeetCode 0166 - Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return sign + str(integer)

        result = [sign + str(integer), "."]
        seen: dict[int, int] = {}
        while remainder:
            if remainder in seen:
                result.insert(seen[remainder], "(")
                result.append(")")
                break
            seen[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(result)
