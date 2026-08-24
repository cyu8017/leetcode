// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution {
    fun minAbsoluteDifference(nums: IntArray): Int {
        var n = nums.size
        var ans = n + 1
        var last = { -ans, -ans, -ans }
        for (i in 0 until n) {
            var x = nums[i]
            if (x != 0) {
                ans = minOf(ans, i - last[3 - x])
                last[x] = i
            }
        }
        if (ans > n) return -1
        return ans
    }
}
