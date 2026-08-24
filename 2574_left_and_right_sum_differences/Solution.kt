// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        var total = 0
        for (x in nums) { total += x }
        var ans = IntArray(nums.size)
        var left = 0
        for (i in 0 until nums.size) {
            var right = total - left - nums[i]
            ans[i] = kotlin.math.abs(left - right)
            left += nums[i]
        }
        return ans
    }
}
