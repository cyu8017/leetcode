# LeetCode 0043 - Multiply Strings
# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        positions = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                low = i + j + 1
                high = i + j
                total = product + positions[low]
                positions[low] = total % 10
                positions[high] += total // 10

        result = "".join(str(d) for d in positions).lstrip("0")
        return result or "0"
