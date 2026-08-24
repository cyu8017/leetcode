# LeetCode 3646 - Next Special Palindrome Number
# https://leetcode.com/problems/next-special-palindrome-number/


class Solution:
    def specialPalindrome(self, n: int) -> int:
        cands = []
        half_cnt = [0] * 10
        mid = 0
        half_len = 0

        def dfs(pos: int, cur: list) -> None:
            if pos == half_len:
                left = "".join(str(d) for d in cur)
                s = left
                if mid > 0:
                    s += str(mid)
                s += left[::-1]
                cands.append(int(s))
                return
            for d in range(1, 10):
                if half_cnt[d] == 0:
                    continue
                half_cnt[d] -= 1
                cur.append(d)
                dfs(pos + 1, cur)
                cur.pop()
                half_cnt[d] += 1

        def gen(mask: int) -> None:
            nonlocal mid, half_len
            total = 0
            odd = 0
            for d in range(1, 10):
                if (mask >> d) & 1:
                    total += d
                    if d % 2 == 1:
                        odd += 1
            if total == 0 or total > 18 or odd > 1:
                return
            for i in range(10):
                half_cnt[i] = 0
            mid = 0
            for d in range(1, 10):
                if ((mask >> d) & 1) == 0:
                    continue
                half_cnt[d] = d // 2
                if d % 2 == 1:
                    mid = d
            half_len = total // 2
            dfs(0, [])

        for mask in range(1, 1 << 10):
            if mask & 1:
                continue
            gen(mask)
        cands.sort()
        for v in cands:
            if v > n:
                return v
        return -1
