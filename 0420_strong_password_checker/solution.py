# LeetCode 0420 - Strong Password Checker
# https://leetcode.com/problems/strong-password-checker/


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        length = len(password)
        missing = 3
        if any(char.islower() for char in password):
            missing -= 1
        if any(char.isupper() for char in password):
            missing -= 1
        if any(char.isdigit() for char in password):
            missing -= 1

        replace = 0
        one_repeat = 0
        two_repeat = 0
        index = 0
        while index < length:
            run = 1
            while index + run < length and password[index + run] == password[index]:
                run += 1
            if run >= 3:
                replace += run // 3
                if run % 3 == 0:
                    one_repeat += 1
                elif run % 3 == 1:
                    two_repeat += 1
            index += run

        if length < 6:
            return max(6 - length, missing)

        if length <= 20:
            return max(missing, replace)

        delete = length - 20
        replace -= min(delete, one_repeat)
        delete -= min(delete, one_repeat)
        replace -= min(delete // 2, two_repeat)
        delete -= min(delete // 2, two_repeat) * 2
        replace -= delete // 3
        return length - 20 + max(missing, replace)
