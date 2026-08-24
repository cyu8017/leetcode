# LeetCode 3662 - Filter Characters by Frequency
# https://leetcode.com/problems/filter-characters-by-frequency/


class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        return "".join(c for c in s if cnt[ord(c) - 97] < k)
