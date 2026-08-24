# LeetCode 3527 - Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/

from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = {}
        for ws in responses:
            seen = set()
            for w in ws:
                if w not in seen:
                    seen.add(w)
                    cnt[w] = cnt.get(w, 0) + 1
        ans = responses[0][0]
        for w, v in cnt.items():
            if cnt[ans] < v or (cnt[ans] == v and w < ans):
                ans = w
        return ans
