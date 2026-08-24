// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

class Solution {
    fun connectTwoGroups(cost: Array<IntArray>): Int {
        val m = cost.size
        val n = cost[0].size
        val full = 1 shl n
        val inf = 1_000_000_000
        var dp = IntArray(full) { inf }
        dp[0] = 0
        for (row in cost) {
            val nxt = IntArray(full) { inf }
            for (mask in 0 until full) {
                if (dp[mask] >= inf) continue
                for (j in 0 until n) {
                    val newMask = mask or (1 shl j)
                    nxt[newMask] = minOf(nxt[newMask], dp[mask] + row[j])
                    nxt[newMask] = minOf(nxt[newMask], nxt[mask] + row[j])
                }
            }
            dp = nxt
        }
        val minimum = IntArray(n)
        for (j in 0 until n) {
            minimum[j] = cost[0][j]
            for (i in 1 until m) minimum[j] = minOf(minimum[j], cost[i][j])
        }
        var ans = inf
        for (mask in 0 until full) {
            var extra = 0
            for (j in 0 until n) {
                if ((mask and (1 shl j)) == 0) extra += minimum[j]
            }
            ans = minOf(ans, dp[mask] + extra)
        }
        return ans
    }
}
