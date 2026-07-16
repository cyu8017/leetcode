# LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        parts = cur = 0
        for x in arr:
            cur += x
            if cur == target:
                parts += 1
                cur = 0
        return parts >= 3
