# LeetCode 2491 - Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        target = skill[0] + skill[n - 1]
        chem = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            chem += skill[i] * skill[n - 1 - i]
        return chem
