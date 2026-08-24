// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

class Solution {
    fun minCost(n: Int, cost: Array<IntArray>): Long {
        val inf = 1L shl 60
        val m = n / 2
        val dp = Array(3) { LongArray(3) }
        for (a in 0 until 3) {
            for (b in 0 until 3) {
                dp[a][b] = if (a == b) inf else cost[0][a].toLong() + cost[n - 1][b]
            }
        }
        for (i in 1 until m) {
            val ndp = Array(3) { LongArray(3) { inf } }
            for (pa in 0 until 3) {
                for (pb in 0 until 3) {
                    if (dp[pa][pb] >= inf) continue
                    for (a in 0 until 3) {
                        if (a == pa) continue
                        for (b in 0 until 3) {
                            if (b == pb || a == b) continue
                            val v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
                            if (v < ndp[a][b]) ndp[a][b] = v
                        }
                    }
                }
            }
            for (a in 0 until 3) for (b in 0 until 3) dp[a][b] = ndp[a][b]
        }
        var ans = inf
        for (a in 0 until 3) for (b in 0 until 3) if (dp[a][b] < ans) ans = dp[a][b]
        return ans
    }
}
