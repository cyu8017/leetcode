// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/


class Solution {
    fun arrayPairSum(nums: IntArray): Int {
        nums.sort()
        var total = 0
        for (i in nums.indices step 2) total += nums[i]
        return total
    }
}
