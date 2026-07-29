// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

class Solution {
    fun longestStrChain(words: Array<String>): Int {
        words.sortBy { it.length }
        val dp = mutableMapOf<String, Int>()
        var ans = 1
        for (w in words) {
            var best = 1
            for (i in w.indices) {
                val prev = w.substring(0, i) + w.substring(i + 1)
                best = maxOf(best, (dp[prev] ?: 0) + 1)
            }
            dp[w] = best
            ans = maxOf(ans, best)
        }
        return ans
    }
}
