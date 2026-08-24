// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution {
    fun numPermsDISequence(s: String): Int {
        val MOD = 1_000_000_007
        val n = s.length
        var dp = IntArray(n + 1) { 1 }
        for (i in 1..n) {
            val newDp = IntArray(n + 1)
            if (s[i - 1] == 'I') {
                var postfix = 0
                for (j in n - i downTo 0) {
                    postfix = (postfix + dp[j + 1]) % MOD
                    newDp[j] = postfix
                }
            } else {
                var prefix = 0
                for (j in 0..n - i) {
                    prefix = (prefix + dp[j]) % MOD
                    newDp[j] = prefix
                }
            }
            dp = newDp
        }
        return dp[0]
    }
}
