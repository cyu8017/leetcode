# LeetCode 2299 - Strong Password Checker II
# https://leetcode.com/problems/strong-password-checker-ii/


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        special = "!@#$%^&*()-+"
        has_lower = has_upper = has_digit = has_special = False
        for i, c in enumerate(password):
            if i > 0 and c == password[i - 1]:
                return False
            if "a" <= c <= "z":
                has_lower = True
            elif "A" <= c <= "Z":
                has_upper = True
            elif "0" <= c <= "9":
                has_digit = True
            elif c in special:
                has_special = True
        return has_lower and has_upper and has_digit and has_special
