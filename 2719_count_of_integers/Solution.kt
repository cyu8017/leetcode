// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

class Solution {
    private val MOD = 1_000_000_007
    private var minSum = 0
    private var maxSum = 0

    fun count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int {
        minSum = min_sum
        maxSum = max_sum
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD
    }

    private fun dec(s: String): String {
        val arr = s.toCharArray()
        var i = arr.size - 1
        while (i >= 0 && arr[i] == '0') {
            arr[i] = '9'
            i--
        }
        if (i >= 0) arr[i] = (arr[i].code - 1).toChar()
        var j = 0
        while (j < arr.size - 1 && arr[j] == '0') j++
        return String(arr, j, arr.size - j)
    }

    private fun dp(s: String): Int {
        val memo = HashMap<String, Int>()
        return dfs(s, 0, 0, true, memo)
    }

    private fun dfs(s: String, pos: Int, sum: Int, tight: Boolean, memo: HashMap<String, Int>): Int {
        if (sum > maxSum) return 0
        if (pos == s.length) return if (sum >= minSum) 1 else 0
        val key = "$pos,$sum,${if (tight) 1 else 0}"
        memo[key]?.let { return it }
        val up = if (tight) s[pos] - '0' else 9
        var res = 0
        for (d in 0..up) {
            res = (res + dfs(s, pos + 1, sum + d, tight && d == up, memo)) % MOD
        }
        memo[key] = res
        return res
    }
}
