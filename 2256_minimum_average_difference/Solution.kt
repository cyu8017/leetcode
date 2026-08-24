// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

class Solution {

    fun minimumAverageDifference(nums: IntArray): Int {

            var n = nums.size
            var total = 0
            for (v in nums) total += v
            var left = 0; var bestDiff = Long.MAX_VALUE
            var bestIdx = 0
            for (i in 0 until n) {
                left += nums[i]
                var leftAvg = left / (i + 1)
                var rightAvg = 0
                if (i != n - 1) rightAvg = (total - left) / (n - i - 1)
                var diff = kotlin.math.abs(leftAvg - rightAvg)
                if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }
            }
            return bestIdx

    }

}
