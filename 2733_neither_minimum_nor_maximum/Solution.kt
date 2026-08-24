// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    fun findNonMinOrMax(nums: IntArray): Int {
        if (nums.size < 3) return -1
        var a = nums[0]
        var b = nums[1]
        var c = nums[2]
        return a + b + c - maxOf(a, maxOf(b, c)) - minOf(a, minOf(b, c))
    }
}
