// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution {
    fun getMinDistance(nums: IntArray, target: Int, start: Int): Int {
        var best = nums.size
        for (i in nums.indices) {
            if (nums[i] == target) best = minOf(best, kotlin.math.abs(i - start))
        }
        return best
    }
}
