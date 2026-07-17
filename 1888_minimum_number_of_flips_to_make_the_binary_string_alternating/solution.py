# LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        alt0 = alt1 = 0

        for i in range(n):
            if doubled[i] != ("0" if i % 2 == 0 else "1"):
                alt0 += 1
            if doubled[i] != ("1" if i % 2 == 0 else "0"):
                alt1 += 1

        answer = min(alt0, alt1)
        for i in range(n):
            if doubled[i] != ("0" if i % 2 == 0 else "1"):
                alt0 -= 1
            if doubled[i + n] != ("0" if (i + n) % 2 == 0 else "1"):
                alt0 += 1

            if doubled[i] != ("1" if i % 2 == 0 else "0"):
                alt1 -= 1
            if doubled[i + n] != ("1" if (i + n) % 2 == 0 else "0"):
                alt1 += 1

            answer = min(answer, alt0, alt1)

        return answer
