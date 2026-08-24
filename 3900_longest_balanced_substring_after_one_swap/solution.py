# LeetCode 3900 - Longest Balanced Substring After One Swap
# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

from typing import Dict, List


class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt0 = 0
        for c in s:
            if c == "0":
                cnt0 += 1
        cnt1 = len(s) - cnt0
        pos: Dict[int, List[int]] = {}
        pos[0] = [-1]
        ans = 0
        pre = 0
        for i in range(len(s)):
            if s[i] == "1":
                pre += 1
            else:
                pre -= 1
            if pre not in pos:
                pos[pre] = []
            pos[pre].append(i)
            ans = max(ans, i - pos[pre][0])
            if pre - 2 in pos:
                p = pos[pre - 2]
                if (i - p[0] - 2) // 2 < cnt0:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
            if pre + 2 in pos:
                p = pos[pre + 2]
                if (i - p[0] - 2) // 2 < cnt1:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
        return ans
