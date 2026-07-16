# LeetCode 0093 - Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result: List[str] = []
        path: List[str] = []

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start : start + length]
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return result
