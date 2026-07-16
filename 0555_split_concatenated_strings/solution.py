# LeetCode 0555 - Split Concatenated Strings
# https://leetcode.com/problems/split-concatenated-strings/

from typing import List


class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        best_forms = [max(s, s[::-1]) for s in strs]
        answer = ""

        for i, original in enumerate(strs):
            mid = "".join(best_forms[i + 1 :] + best_forms[:i])
            for candidate in (original, original[::-1]):
                for cut in range(len(candidate)):
                    formed = candidate[cut:] + mid + candidate[:cut]
                    if formed > answer:
                        answer = formed

        return answer
