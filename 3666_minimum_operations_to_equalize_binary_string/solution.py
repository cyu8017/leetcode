# LeetCode 3666 - Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ts = [set(), set()]
        for i in range(n + 1):
            ts[i % 2].add(i)
        cnt0 = s.count("0")
        ts[cnt0 % 2].discard(cnt0)
        q = [cnt0]
        ans = 0
        while q:
            nq = []
            for cur in q:
                if cur == 0:
                    return ans
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                t = ts[l % 2]
                for it in sorted(t):
                    if it < l:
                        continue
                    if it > r:
                        break
                    nq.append(it)
                    t.discard(it)
            q = nq
            ans += 1
        return -1
