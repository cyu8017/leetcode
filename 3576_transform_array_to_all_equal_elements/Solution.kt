// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution {
    fun canMakeEqual(nums: IntArray, k: Int): Boolean {
        return check(nums, nums[0], k) || check(nums, -nums[0], k)
    }

    fun check(nums: IntArray, target: Int, kk: Int): Boolean {
        var cnt = 0
        var sign = 1
        for (i in 0 until nums.size - 1) {
            var x = nums[i] * sign
            if (x == target) sign = 1
            else {
                sign = -1
                cnt = cnt + 1
            }
        }
        return cnt <= kk && nums[nums.size - 1] * sign == target
    }
}
