// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

class Solution {
    fun maxUncrossedLines(nums1: IntArray, nums2: IntArray): Int {
        val m = nums1.size; val n = nums2.size
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (i in 1..m) {
            for (j in 1..n) {
                dp[i][j] = if (nums1[i - 1] == nums2[j - 1]) dp[i - 1][j - 1] + 1
                else maxOf(dp[i - 1][j], dp[i][j - 1])
            }
        }
        return dp[m][n]
    }
}
