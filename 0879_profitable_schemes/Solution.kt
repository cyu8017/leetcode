// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

class Solution {
    fun profitableSchemes(n: Int, minProfit: Int, group: IntArray, profit: IntArray): Int {
        val MOD = 1_000_000_007
        var dp = Array(n + 1) { IntArray(minProfit + 1) }
        dp[0][0] = 1
        for (i in 0 until group.size) {
            var members = group[i]
            var p = profit[i]
            for (people in n downTo members) {
                for (prof in minProfit downTo 0) {
                    var np = minOf(minProfit, prof + p)
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD
                }
            }
        }
        var ans = 0
        for (people in 0 until = n) { ans = (ans + dp[people][minProfit]) % MOD }
        return ans
    }
}
