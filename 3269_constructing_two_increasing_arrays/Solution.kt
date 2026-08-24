// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

class Solution {
    fun minLargest(nums1: IntArray, nums2: IntArray): Int {
        var n = nums1.size
        var m = nums2.size
        val inf = 1000000000
        var dp = IntArray(n + 1)[]
        for (i in 0 ..n) {
            dp[i] = IntArray(m + 1)
            for (j in 0 ..m) { dp[i][j] = inf }
        }
        dp[0][0] = 0
        for (i in 0 ..n) {
            for (j in 0 ..m) {
                if (dp[i][j] == inf) continue
                var prev = dp[i][j]
                if (i < n) {
                    var need = prev + 1
                    if (nums1[i] == 0) {
                        if (need % 2 != 0) need++
                    } else {
                        if (need % 2 == 0) need++
                    }
                    if (need < dp[i + 1][j]) dp[i + 1][j] = need
                }
                if (j < m) {
                    var need = prev + 1
                    if (nums2[j] == 0) {
                        if (need % 2 != 0) need++
                    } else {
                        if (need % 2 == 0) need++
                    }
                    if (need < dp[i][j + 1]) dp[i][j + 1] = need
                }
            }
        }
        return dp[n][m]
    }
}
