// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

import kotlin.math.abs

class Solution {
    fun longestIdealString(s: String, k: Int): Int {
        val dp = IntArray(26)
        var ans = 0
        for (ch in s) {
            val c = ch - 'a'
            var best = 0
            for (p in 0 until 26) {
                if (abs(c - p) <= k && dp[p] > best) best = dp[p]
            }
            dp[c] = best + 1
            ans = maxOf(ans, dp[c])
        }
        return ans
    }
}
