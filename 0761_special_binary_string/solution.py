# LeetCode 0761 - Special Binary String
# https://leetcode.com/problems/special-binary-string/


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts: list[str] = []
        balance = start = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == "1" else -1
            if balance == 0:
                parts.append("1" + self.makeLargestSpecial(s[start + 1 : i]) + "0")
                start = i + 1
        return "".join(sorted(parts, reverse=True))
