# LeetCode 3280 - Convert Date to Binary
# https://leetcode.com/problems/convert-date-to-binary/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def toBinary(v: int) -> str:
            if v == 0:
                return "0"
            s = ""
            while v > 0:
                s = str(v & 1) + s
                v >>= 1
            return s

        parts = date.split("-")
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        return toBinary(y) + "-" + toBinary(m) + "-" + toBinary(d)
