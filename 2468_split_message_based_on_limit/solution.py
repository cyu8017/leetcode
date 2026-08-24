# LeetCode 2468 - Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/

from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        for parts in range(1, n + 1):
            sb_digits = len(str(parts))
            ok = True
            idx = 0
            res = []
            for i in range(1, parts + 1):
                tail = 3 + len(str(i)) + sb_digits
                cap = limit - tail
                if cap <= 0 or idx >= n:
                    ok = False
                    break
                take = cap
                if take > n - idx:
                    take = n - idx
                res.append(message[idx : idx + take] + "<" + str(i) + "/" + str(parts) + ">")
                idx += take
            if ok and idx == n:
                return res
        return []
