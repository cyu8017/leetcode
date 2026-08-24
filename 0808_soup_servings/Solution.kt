// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

class Solution {
    private var memo: MutableMap<Long, Double>? = null

    fun soupServings(n: Int): Double {
        if (n >= 4800) return 1.0
        var units = (n + 24) / 25
        memo = HashMap()
        return dp(units, units)
    }

    private fun dp(a: Int, b: Int): Double {
        if (a <= 0 && b <= 0) return 0.5
        if (a <= 0) return 1.0
        if (b <= 0) return 0.0
        var key = (a  shl  16) | b
        if (memo.containsKey(key)) return memo[key]
        var `val` = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
        memo[key] = val
        return val
    }
}
