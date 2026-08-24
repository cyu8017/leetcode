# LeetCode 3714 - Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/


class Solution:
    def longestBalanced(self, s: str) -> int:
        def calc1(st: str) -> int:
            res = 0
            n = len(st)
            i = 0
            while i < n:
                j = i + 1
                while j < n and st[j] == st[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        def calc2(st: str, a: str, b: str) -> int:
            res = 0
            n = len(st)
            i = 0
            while i < n:
                while i < n and st[i] != a and st[i] != b:
                    i += 1
                pos = {0: i - 1}
                d = 0
                while i < n and (st[i] == a or st[i] == b):
                    if st[i] == a:
                        d += 1
                    else:
                        d -= 1
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res

        def calc3(st: str) -> int:
            pos = {"0,0": -1}
            cnt = [0, 0, 0]
            res = 0
            for i, ch in enumerate(st):
                cnt[ord(ch) - 97] += 1
                x = cnt[0] - cnt[1]
                y = cnt[1] - cnt[2]
                k = f"{x},{y}"
                if k in pos:
                    res = max(res, i - pos[k])
                else:
                    pos[k] = i
            return res

        x = calc1(s)
        y = max(calc2(s, "a", "b"), calc2(s, "b", "c"), calc2(s, "a", "c"))
        z = calc3(s)
        return max(x, y, z)
