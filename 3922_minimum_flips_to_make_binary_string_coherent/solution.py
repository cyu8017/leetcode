# LeetCode 3922 - Minimum Flips to Make Binary String Coherent
# https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/


class Solution:
    def minFlips(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        answer = ones
        if ones > 0:
            answer = ones - 1
        zeros = len(s) - ones
        answer = min(answer, zeros)
        if len(s) >= 2:
            cost = 0
            for i in range(len(s)):
                want = "1" if (i == 0 or i == len(s) - 1) else "0"
                if s[i] != want:
                    cost += 1
            answer = min(answer, cost)
        return answer
