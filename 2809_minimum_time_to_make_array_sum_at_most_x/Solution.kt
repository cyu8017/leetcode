// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
    fun minimumTime(nums1: MutableList<Int>, nums2: MutableList<Int>, x: Int): Int {
        val n = nums1.size
        val arr = Array(n) { IntArray(2) }
        var sum1 = 0
        var sum2 = 0
        for (i in 0 until n) {
            arr[i][0] = nums1[i]
            arr[i][1] = nums2[i]
            sum1 += nums1[i]
            sum2 += nums2[i]
        }
        arr.sortWith(compareBy { it[1] })
        val dp = IntArray(n + 1)
        for (i in 0 until n) {
            for (j in (i + 1) downTo 1) {
                dp[j] = maxOf(dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1])
            }
        }
        for (t in 0..n) {
            if (sum1 + sum2 * t - dp[t] <= x) return t
        }
        return -1
    }
}
