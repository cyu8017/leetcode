// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

class Solution {
    fun rob(nums: IntArray): Int {
        if (nums.size == 1) return nums[0]
        return maxOf(robLinear(nums, 0, nums.size - 1), robLinear(nums, 1, nums.size))
    }

    private fun robLinear(nums: IntArray, start: Int, end: Int): Int {
        var prev2 = 0
        var prev1 = 0
        for (i in start until end) {
            val current = maxOf(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        }
        return prev1
    }
}
