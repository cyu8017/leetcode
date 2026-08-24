// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

class Solution {
    fun countGoodIntegers(l: Long, r: Long, k: Int): Long {
        return count(r, k) - count(l - 1, k)
    }

    private fun count(bound: Long, k: Int): Long {
        if (bound <= 0) return 0
        val digits = bound.toString()
        val memo = HashMap<String, Long>()
        return dfs(0, 0, false, true, digits, k, memo)
    }

    private fun dfs(position: Int, previous: Int, started: Boolean, tight: Boolean, digits: String, k: Int, memo: HashMap<String, Long>): Long {
        if (position == digits.length) return if (started) 1 else 0
        val key = "$position,$previous,$started"
        if (!tight && memo.containsKey(key)) return memo[key]!!
        val limit = if (tight) digits[position] - '0' else 9
        var result = 0L
        for (digit in 0..limit) {
            val nextStarted = started || digit != 0
            if (started && kotlin.math.abs(previous - digit) > k) continue
            val nextPrevious = if (nextStarted) digit else previous
            result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit, digits, k, memo)
        }
        if (!tight) memo[key] = result
        return result
    }
}
