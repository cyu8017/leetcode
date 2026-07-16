# LeetCode 0906 - Super Palindromes
# https://leetcode.com/problems/super-palindromes/

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)

        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True

        def valid_root(pal: int, odd_root: bool) -> bool:
            if odd_root and len(str(pal)) == 1:
                return pal in (2, 3, 5)
            return is_prime(pal)

        ans = 0
        if L <= 1 <= R:
            ans += 1
        for k in range(1, 10**5 + 1):
            s = str(k)
            pal = int(s + s[::-1])
            sq = pal * pal
            if sq > R:
                break
            if sq >= L and valid_root(pal, False):
                ans += 1
        for k in range(1, 10**5 + 1):
            s = str(k)
            pal = int(s + s[:-1][::-1])
            sq = pal * pal
            if sq > R:
                break
            if sq >= L and valid_root(pal, True):
                ans += 1
        return ans
