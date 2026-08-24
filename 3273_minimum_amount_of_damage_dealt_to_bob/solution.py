# LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

from functools import cmp_to_key
from typing import List


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        arr = []
        totalDmg = 0
        for i in range(n):
            hits = (health[i] + power - 1) // power
            arr.append({"dmg": damage[i], "hits": hits})
            totalDmg += damage[i]
        arr.sort(key=cmp_to_key(lambda a, b: a["hits"] * b["dmg"] - b["hits"] * a["dmg"]))
        ans, cur = 0, totalDmg
        for e in arr:
            ans += cur * e["hits"]
            cur -= e["dmg"]
        return ans
