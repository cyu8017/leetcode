// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution {
    fun minimumAverage(nums: IntArray): Double {
        nums.sort()
        var n = nums.size
        var ans = 1  shl  30
        for (i in 0 until n / 2) { ans = minOf(ans, nums[i] + nums[n - i - 1]) }
        return ans / 2.0
    }
}
