// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    fun rob(nums: IntArray, colors: IntArray): Long {
        var n = nums.size
        var f = 0
        var g = nums[0]
        for (i in 1 until n) {
            if (colors[i - 1] == colors[i]) {
                var nf = maxOf(f, g)
                g = f + nums[i]
                f = nf
            } else {
                var nf = maxOf(f, g)
                g = nf + nums[i]
                f = nf
            }
        }
        return maxOf(f, g)
    }
}
