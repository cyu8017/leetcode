# LeetCode 2383 - Minimum Hours of Training to Win a Competition
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

from typing import List


class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        ans = 0
        en, ex = initialEnergy, initialExperience
        for i in range(len(energy)):
            if en <= energy[i]:
                need = energy[i] - en + 1
                ans += need
                en += need
            if ex <= experience[i]:
                need = experience[i] - ex + 1
                ans += need
                ex += need
            en -= energy[i]
            ex += experience[i]
        return ans
