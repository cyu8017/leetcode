// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution {
    fun maxAdjacentDistance(nums: IntArray): Int {
        var ans = 0
        var n = nums.size
        for (i in 0 until n) {
            var d = kotlin.math.abs(nums[i] - nums[(i + 1) % n])
            if (d > ans) ans = d
        }
        return ans
    }
}
