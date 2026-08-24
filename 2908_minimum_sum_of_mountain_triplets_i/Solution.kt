// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/


class Solution {
    fun minimumSum(nums: IntArray): Int {
        val n = nums.size
        var ans = 1 shl 30
        for (j in 1 until n - 1) {
            var left = 1 shl 30
            var right = 1 shl 30
            for (i in 0 until j) if (nums[i] < nums[j] && nums[i] < left) left = nums[i]
            for (k in j + 1 until n) if (nums[k] < nums[j] && nums[k] < right) right = nums[k]
            if (left < (1 shl 30) && right < (1 shl 30)) {
                val cand = left + nums[j] + right
                if (cand < ans) ans = cand
            }
        }
        return if (ans == (1 shl 30)) -1 else ans
    }
}
