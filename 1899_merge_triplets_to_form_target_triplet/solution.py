# LeetCode 1899 - Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        merged = [0, 0, 0]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                merged[0] = max(merged[0], a)
                merged[1] = max(merged[1], b)
                merged[2] = max(merged[2], c)
        return merged == target
