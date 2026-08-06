// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

class Solution {
    fun minDistance(houses: IntArray, k: Int): Int {
        houses.sort()
        val n = houses.size
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in i until n) {
                val mid = houses[(i + j) / 2]
                var sum = 0
                for (t in i..j) sum += kotlin.math.abs(houses[t] - mid)
                cost[i][j] = sum
            }
        }
        var dp = LongArray(n + 1) { if (it == 0) 0 else 1e15.toLong() }
        repeat(k) {
            val ndp = LongArray(n + 1) { if (it == 0) 0 else 1e15.toLong() }
            for (j in 1..n) {
                var best = 1e15.toLong()
                for (i in 0 until j) best = minOf(best, dp[i] + cost[i][j - 1])
                ndp[j] = best
            }
            dp = ndp
        }
        return dp[n].toInt()
    }
}
