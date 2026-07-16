class Solution:
    def toHexspeak(self, num: str) -> str:
        value = int(num)
        digits = "0123456789ABCDEF"
        out = ""
        while value:
            value, rem = divmod(value, 16)
            if 2 <= rem <= 9:
                return "ERROR"
            out = digits[rem] + out
        return (out or "0").replace("0", "O").replace("1", "I")
