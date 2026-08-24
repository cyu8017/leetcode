// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/


class Solution {
    fun kInversePairs(n: Int, k: Int): Int {
        val MOD = 1_000_000_007
        var dp = IntArray(k + 1)
        dp[0] = 1
        for (len in 1..n) {
            val nxt = IntArray(k + 1)
            var prefix = 0L
            for (inv in 0..k) {
                prefix += dp[inv]
                if (inv >= len) prefix -= dp[inv - len]
                prefix = (prefix % MOD + MOD) % MOD
                nxt[inv] = prefix.toInt()
            }
            dp = nxt
        }
        return dp[k]
    }
}
