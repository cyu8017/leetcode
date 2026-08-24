// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

import kotlin.math.abs

class Solution {
    private val mod = 1_000_000_007
    private lateinit var memo: Array<IntArray>
    private lateinit var locations: IntArray
    private var finish = 0

    fun countRoutes(locations: IntArray, start: Int, finish: Int, fuel: Int): Int {
        this.locations = locations
        this.finish = finish
        memo = Array(locations.size) { IntArray(fuel + 1) { -1 } }
        return dp(start, fuel)
    }

    private fun dp(city: Int, left: Int): Int {
        if (memo[city][left] != -1) return memo[city][left]
        var total = if (city == finish) 1L else 0L
        for (nxt in locations.indices) {
            val cost = abs(locations[city] - locations[nxt])
            if (nxt != city && cost <= left) {
                total += dp(nxt, left - cost)
            }
        }
        memo[city][left] = (total % mod).toInt()
        return memo[city][left]
    }
}
