// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
    private val MOD = 1_000_000_007

    fun countSteppingNumbers(low: String, high: String): Int {
        var ans = (countTo(high) - countTo(dec(low))) % MOD
        if (ans < 0) ans += MOD
        return ans
    }

    private fun countTo(s: String): Int {
        val memo = Array(85) { Array(2) { Array(11) { IntArray(2) { -1 } } } }
        return dfs(s, 0, 1, -1, 0, memo)
    }

    private fun dfs(
        s: String,
        pos: Int,
        tight: Int,
        last: Int,
        started: Int,
        memo: Array<Array<Array<IntArray>>>
    ): Int {
        if (pos == s.length) return started
        if (memo[pos][tight][last + 1][started] != -1) return memo[pos][tight][last + 1][started]
        val up = if (tight == 1) s[pos] - '0' else 9
        var ans = 0L
        for (d in 0..up) {
            val nt = if (tight == 1 && d == up) 1 else 0
            if (started == 0) {
                ans += if (d == 0) dfs(s, pos + 1, nt, -1, 0, memo)
                else dfs(s, pos + 1, nt, d, 1, memo)
            } else if (kotlin.math.abs(d - last) == 1) {
                ans += dfs(s, pos + 1, nt, d, 1, memo)
            }
        }
        val res = (ans % MOD).toInt()
        memo[pos][tight][last + 1][started] = res
        return res
    }

    private fun dec(s: String): String {
        val arr = s.toCharArray()
        var i = arr.size - 1
        while (i >= 0 && arr[i] == '0') {
            arr[i] = '9'
            i--
        }
        if (i >= 0) arr[i]--
        var j = 0
        while (j < arr.size - 1 && arr[j] == '0') j++
        return String(arr, j, arr.size - j)
    }
}
