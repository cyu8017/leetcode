# LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping

class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer, i = [], len(s) - 1
        while i >= 0:
            if s[i] == "#":
                answer.append(chr(96 + int(s[i - 2:i]))); i -= 3
            else:
                answer.append(chr(96 + int(s[i]))); i -= 1
        return "".join(reversed(answer))
