# LeetCode 1079 - Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs() -> int:
            total = 0
            for ch, freq in count.items():
                if freq == 0:
                    continue
                count[ch] -= 1
                total += 1 + dfs()
                count[ch] += 1
            return total

        return dfs()
