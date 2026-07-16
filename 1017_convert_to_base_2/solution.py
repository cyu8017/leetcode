# LeetCode 1017 - Convert to Base -2
# https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans: list[str] = []
        while n:
            n, rem = divmod(n, -2)
            if rem < 0:
                n += 1
                rem += 2
            ans.append(str(rem))
        return "".join(reversed(ans))
