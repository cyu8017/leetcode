// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution {
    fun checkEqualPartitions(nums: IntArray, target: Long): Boolean {
        var n = nums.size
        for (i in 0 until (1  shl  n)) {
            var x = 1
            var y = 1
            for (j in 0 until n) {
                if (((i  shr  j) & 1) != 0) x *= nums[j]
                else y *= nums[j]
                if (x > target || y > target) break
            }
            if (x == target && y == target) return true
        }
        return false
    }
}
