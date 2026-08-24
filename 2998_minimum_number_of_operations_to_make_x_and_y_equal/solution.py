# LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        q = [[x, 0]]
        seen = {x}
        qi = 0
        while qi < len(q):
            v, d = q[qi]
            qi += 1
            if v == y:
                return d
            cands = [v + 1, v - 1, (v // 11) if v % 11 == 0 else -1, (v // 5) if v % 5 == 0 else -1]
            for nxt in cands:
                if nxt > 0 and nxt < 2 * x + 20 and nxt not in seen:
                    seen.add(nxt)
                    q.append([nxt, d + 1])
        return -1
