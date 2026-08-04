// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

class Solution {
    fun minDays(n: Int): Int = dp(n, HashMap())

    private fun dp(x: Int, memo: HashMap<Int, Int>): Int {
        if (x <= 1) return x
        memo[x]?.let { return it }
        val a = x % 2 + dp(x / 2, memo)
        val b = x % 3 + dp(x / 3, memo)
        val result = 1 + minOf(a, b)
        memo[x] = result
        return result
    }
}
