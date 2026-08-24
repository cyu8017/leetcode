// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
    fun numberOfWays(n: Int, x: Int): Int {
        val MOD = 1_000_000_007
        val powers = ArrayList<Int>()
        var i = 1
        while (true) {
            var p = 1L
            for (j in 0 until x) {
                p *= i
                if (p > n) break
            }
            if (p > n) break
            powers.add(p.toInt())
            i++
        }
        val dp = IntArray(n + 1)
        dp[0] = 1
        for (p in powers) {
            for (s in n downTo p) {
                dp[s] = (dp[s] + dp[s - p]) % MOD
            }
        }
        return dp[n]
    }
}
