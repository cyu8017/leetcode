# LeetCode 3758 - Convert Number Words to Digits
# https://leetcode.com/problems/convert-number-words-to-digits/

class Solution:
    def convertNumber(self, s: str) -> str:
        d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        n = len(s)
        ans = []
        i = 0
        while i < n:
            for j in range(10):
                m = len(d[j])
                if i + m <= n and s[i:i + m] == d[j]:
                    ans.append(chr(48 + j))
                    i += m - 1
                    break
            i += 1
        return "".join(ans)
