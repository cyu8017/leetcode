# LeetCode 2376 - Count Special Integers
# https://leetcode.com/problems/count-special-integers/

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        m = len(s)
        ans = 0
        perm = 9
        for i in range(1, m):
            ans += perm
            perm *= 10 - i
        used = [False] * 10
        for i in range(m):
            start = 1 if i == 0 else 0
            digit = ord(s[i]) - 48
            for d in range(start, digit):
                if used[d]:
                    continue
                rem = 10 - (i + 1)
                ways = 1
                for _ in range(i + 1, m):
                    ways *= rem
                    rem -= 1
                ans += ways
            if used[digit]:
                return ans
            used[digit] = True
        return ans + 1
