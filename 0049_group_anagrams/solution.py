# LeetCode 0049 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple[str, ...], list[str]] = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)

        result = [sorted(group) for group in groups.values()]
        result.sort(key=lambda group: min(strs.index(word) for word in group), reverse=True)
        return result
