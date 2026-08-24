// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
    fun numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int {
        return count(high, k) - count(low - 1, k)
    }

    private fun count(n: Int, k: Int): Int {
        if (n < 0) return 0
        val s = n.toString()
        val memo = Array(12) {
            Array(45) { Array(22) { Array(2) { IntArray(2) { -1 } } } }
        }
        return dfs(s, k, 0, 0, 0, 1, 0, memo)
    }

    private fun dfs(
        s: String,
        k: Int,
        pos: Int,
        diff: Int,
        mod: Int,
        tight: Int,
        started: Int,
        memo: Array<Array<Array<Array<IntArray>>>>
    ): Int {
        if (pos == s.length) return if (started == 1 && diff == 0 && mod == 0) 1 else 0
        if (memo[pos][diff + 20][mod][tight][started] != -1) {
            return memo[pos][diff + 20][mod][tight][started]
        }
        val up = if (tight == 1) s[pos] - '0' else 9
        var ans = 0
        for (digit in 0..up) {
            val nt = if (tight == 1 && digit == up) 1 else 0
            if (started == 0) {
                if (digit == 0) {
                    ans += dfs(s, k, pos + 1, diff, mod, nt, 0, memo)
                } else {
                    val nd = diff + if (digit % 2 == 0) 1 else -1
                    ans += dfs(s, k, pos + 1, nd, digit % k, nt, 1, memo)
                }
            } else {
                val nd = diff + if (digit % 2 == 0) 1 else -1
                ans += dfs(s, k, pos + 1, nd, (mod * 10 + digit) % k, nt, 1, memo)
            }
        }
        memo[pos][diff + 20][mod][tight][started] = ans
        return ans
    }
}
