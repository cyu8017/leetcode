// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    fun dieSimulator(n: Int, rollMax: IntArray): Int {
        val mod = 1_000_000_007
        var dp = Array(6) { j -> IntArray(rollMax[j] + 1).also { it[1] = 1 } }
        repeat(n - 1) {
            val totals = IntArray(6)
            for (j in 0 until 6) {
                for (run in 1 until dp[j].size) totals[j] = (totals[j] + dp[j][run]) % mod
            }
            val nxt = Array(6) { j ->
                IntArray(dp[j].size).also { row ->
                    var sumOthers = 0
                    for (k in 0 until 6) if (k != j) sumOthers = (sumOthers + totals[k]) % mod
                    row[1] = sumOthers
                    for (run in 2 until dp[j].size) row[run] = dp[j][run - 1]
                }
            }
            dp = nxt
        }
        var ans = 0
        for (j in 0 until 6) {
            for (run in 1 until dp[j].size) ans = (ans + dp[j][run]) % mod
        }
        return ans
    }
}
