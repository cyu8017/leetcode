// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
    fun maximumJumps(nums: IntArray, target: Int): Int {
        var n = nums.size
        var dp = IntArray(n)
        dp.fill(-1)
        dp[0] = 0
        for (i in 0 until n) {
            if (dp[i] < 0) continue
            for (j in i + 1 until n) {
                if (kotlin.math.abs(nums[j] - nums[i]) <= target)
                    dp[j] = maxOf(dp[j], dp[i] + 1)
            }
        }
        return dp[n - 1]
    }
}
