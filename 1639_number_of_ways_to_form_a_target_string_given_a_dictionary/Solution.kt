// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution {
    fun numWays(words: Array<String>, target: String): Int {
        val MOD = 1_000_000_007L
        val m = words[0].length
        val dp = LongArray(target.length + 1)
        dp[0] = 1L
        for (j in 0 until m) {
            val count = IntArray(26)
            for (word in words) count[word[j] - 'a']++
            for (i in minOf(j + 1, target.length) downTo 1) {
                dp[i] = (dp[i] + dp[i - 1] * count[target[i - 1] - 'a']) % MOD
            }
        }
        return dp[target.length].toInt()
    }
}
