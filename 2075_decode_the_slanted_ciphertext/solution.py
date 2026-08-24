# LeetCode 2075 - Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        cols = len(encodedText) // rows
        b = []
        for c in range(cols):
            for r in range(rows):
                if c + r >= cols:
                    break
                b.append(encodedText[r * cols + c + r])
        while b and b[-1] == " ":
            b.pop()
        return "".join(b)
