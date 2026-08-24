// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

class Solution {
    private var x = 0
    private val memo = HashMap<Int, Int>()

    fun leastOpsExpressTarget(x: Int, target: Int): Int {
        this.x = x
        return dfs(target)
    }

    private fun dfs(t: Int): Int {
        memo[t]?.let { return it }
        if (x > t) {
            val ans = minOf(2 * t - 1, 2 * (x - t))
            memo[t] = ans
            return ans
        }
        if (x == t) {
            memo[t] = 0
            return 0
        }
        var prod = x.toLong()
        var n = 0
        while (prod < t) {
            prod *= x
            n++
        }
        if (prod == t.toLong()) {
            memo[t] = n
            return n
        }
        var ans = dfs(t - (prod / x).toInt()) + n
        if (prod < 2L * t) ans = minOf(ans, dfs(prod.toInt() - t) + n + 1)
        memo[t] = ans
        return ans
    }
}
