// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

class Solution {
    fun assignBikes(workers: Array<IntArray>, bikes: Array<IntArray>): Int {
        val memo = Array(workers.size) { IntArray(1 shl bikes.size) { -1 } }
        return dp(0, 0, workers, bikes, memo)
    }

    private fun dp(i: Int, mask: Int, workers: Array<IntArray>, bikes: Array<IntArray>, memo: Array<IntArray>): Int {
        if (i == workers.size) return 0
        if (memo[i][mask] != -1) return memo[i][mask]
        var best = Int.MAX_VALUE
        val wx = workers[i][0]
        val wy = workers[i][1]
        for (b in bikes.indices) {
            if ((mask and (1 shl b)) != 0) continue
            val dist = kotlin.math.abs(wx - bikes[b][0]) + kotlin.math.abs(wy - bikes[b][1])
            best = minOf(best, dist + dp(i + 1, mask or (1 shl b), workers, bikes, memo))
        }
        memo[i][mask] = best
        return best
    }
}
