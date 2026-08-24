// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

class Solution {
    fun maxScore(a: IntArray, b: IntArray): Long {
        var neg = -(1L  shl  62)
        var dp = longArrayOf( 0, neg, neg, neg, neg )
        for (x in b) {
            for (k in 4 downTo 1) {
                if (dp[k - 1] == neg) continue
                var v = dp[k - 1] + a[k - 1] * x
                if (v > dp[k]) dp[k] = v
            }
        }
        return dp[4]
    }
}
