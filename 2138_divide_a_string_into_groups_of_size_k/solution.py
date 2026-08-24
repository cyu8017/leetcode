# LeetCode 2138 - Divide a String Into Groups of Size k
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

from typing import List, Any
class Solution:
    def divideString(self, s: str, k: int, fill: Any) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            if i + k <= len(s):
                ans.append(s[i:i + k])
            else:
                chunk = s[i:]
                while len(chunk) < k:
                    chunk += fill
                ans.append(chunk)
        return ans
