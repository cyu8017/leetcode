// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

class Solution {
    fun minOperations(s1: String, s2: String): Int {
        val infinity = 1000000000
        var dp = intArrayOf(0, infinity)
        val n = s1.length
        for (i in 0 until n) {
            val next = intArrayOf(infinity, infinity)
            for (forcedZero in 0..1) {
                if (dp[forcedZero] == infinity) continue
                var current = s1[i]
                if (forcedZero == 1) current = '0'
                var direct = dp[forcedZero]
                if (current == '0' && s2[i] == '1') direct++
                else if (current == '1' && s2[i] == '0') direct = infinity
                next[0] = minOf(next[0], direct)
                if (i + 1 < n) {
                    var cost = dp[forcedZero] + 1
                    if (current == '0') cost++
                    if (s1[i + 1] == '0') cost++
                    if (s2[i] == '1') cost++
                    next[1] = minOf(next[1], cost)
                }
            }
            dp = next
        }
        return if (dp[0] == infinity) -1 else dp[0]
    }
}
