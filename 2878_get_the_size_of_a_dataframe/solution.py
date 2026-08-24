# LeetCode 2878 - Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe/

from typing import Any, List


class Solution:
    def getDataframeSize(self, players: Any) -> List[int]:
        if not players:
            return [0, 0]
        rows = len(players)
        first = players[0]
        cols = len(first) if isinstance(first, list) else len(first.keys())
        return [rows, cols]
