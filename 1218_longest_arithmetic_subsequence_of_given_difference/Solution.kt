// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution {
    fun longestSubsequence(arr: IntArray, difference: Int): Int {
        val dp = mutableMapOf<Int, Int>()
        var ans = 0
        for (x in arr) {
            val len = dp.getOrDefault(x - difference, 0) + 1
            dp[x] = len
            ans = maxOf(ans, len)
        }
        return ans
    }
}
