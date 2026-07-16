# LeetCode 0506 - Relative Ranks
# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        medals = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        order = sorted(range(len(score)), key=lambda index: -score[index])
        result = [""] * len(score)
        for rank, index in enumerate(order, start=1):
            result[index] = medals.get(rank, str(rank))
        return result
