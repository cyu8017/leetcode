# LeetCode 3703 - Remove K-Balanced Substrings
# https://leetcode.com/problems/remove-k-balanced-substrings/


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            if c == ")" and len(stk) > 1:
                top = stk[-1]
                prev = stk[-2]
                if top[1] == k and prev[1] >= k:
                    stk.pop()
                    prev[1] -= k
                    if prev[1] == 0:
                        stk.pop()
        return "".join(p[0] * p[1] for p in stk)
