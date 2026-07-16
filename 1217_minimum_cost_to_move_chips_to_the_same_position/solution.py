class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd = sum(x & 1 for x in position)
        return min(odd, len(position) - odd)
