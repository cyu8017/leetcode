// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

class Solution {
    fun minimizeSum(nums: IntArray): Int {
        nums.sort()
        var n = nums.size
        var a = nums[n - 1] - nums[2]
        var b = nums[n - 3] - nums[0]
        var c = nums[n - 2] - nums[1]
        return minOf(a, minOf(b, c))
    }
}
