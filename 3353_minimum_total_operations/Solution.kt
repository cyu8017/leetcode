// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var ops = 0
        for (i in nums.size - 2 downTo 0) {
            if (nums[i] != nums[i + 1]) ops++
        }
        return ops
    }
}
