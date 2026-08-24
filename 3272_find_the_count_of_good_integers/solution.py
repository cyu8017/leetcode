# LeetCode 3272 - Find the Count of Good Integers
# https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        start = 1
        for i in range(1, half):
            start *= 10
        end = start * 10
        seen = set()
        ans = 0
        fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        for h in range(start, end):
            s = str(h)
            pal = s
            revStart = len(s) - 1
            if n % 2 == 1:
                revStart -= 1
            for i in range(revStart, -1, -1):
                pal += s[i]
            if int(pal) % k != 0:
                continue
            chars = "".join(sorted(pal))
            if chars in seen:
                continue
            seen.add(chars)
            cnt = [0] * 10
            for c in chars:
                cnt[ord(c) - 48] += 1
            total = fact[n]
            for c in cnt:
                total //= fact[c]
            if cnt[0] > 0:
                bad = fact[n - 1]
                cnt[0] -= 1
                for c in cnt:
                    bad //= fact[c]
                cnt[0] += 1
                total -= bad
            ans += total
        return ans
