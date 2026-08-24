# LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

from typing import List


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        cnt = [0, 0]
        for c in t:
            cnt[ord(c) - 48] += 1
        ans: List[str] = [""] * len(s)
        for i in range(len(s)):
            x = ord(s[i]) - 48
            if cnt[x ^ 1] > 0:
                cnt[x ^ 1] -= 1
                ans[i] = "1"
            else:
                cnt[x] -= 1
                ans[i] = "0"
        return "".join(ans)
