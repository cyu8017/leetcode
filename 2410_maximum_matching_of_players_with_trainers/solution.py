# LeetCode 2410 - Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        i = j = ans = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans
