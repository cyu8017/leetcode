// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution {
    fun absDifference(nums: IntArray, k: Int): Int {
        nums.sort()
        var ans = 0
        var n = nums.size
        for (i in 0 until k) { ans += nums[n - i - 1] - nums[i] }
        return ans
    }
}
