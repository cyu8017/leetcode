# LeetCode 2271 - Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1)
        ans = 0
        j = 0
        for i in range(n):
            end = tiles[i][0] + carpetLen - 1
            while j < n and tiles[j][0] <= end:
                j += 1
            cover = pref[j] - pref[i]
            if j > 0 and tiles[j - 1][1] > end:
                cover -= tiles[j - 1][1] - end
            ans = max(ans, cover)
        return ans
