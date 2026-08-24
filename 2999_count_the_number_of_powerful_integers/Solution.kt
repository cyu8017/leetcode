// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

class Solution {
    private lateinit var s: String
    private var limit = 0

    private fun count(num: Long): Long {
        if (num < 0) return 0
        for (i in s.indices) if (s[i] - '0' > limit) return 0
        val t = num.toString()
        val n = t.length
        val sn = s.length
        if (n < sn) return 0
        var ans = 0L
        for (length in sn until n) {
            val preLen = length - sn
            if (preLen == 0) ans += 1
            else {
                var ways = limit.toLong()
                for (i in 1 until preLen) ways *= (limit + 1)
                ans += ways
            }
        }
        val pref = n - sn
        val memo = HashMap<Long, Long>()
        ans += dfs(t, pref, 0, true, memo)
        return ans
    }

    private fun dfs(t: String, pref: Int, i: Int, tight: Boolean, memo: HashMap<Long, Long>): Long {
        if (i == pref) {
            if (tight) return if (t.substring(pref).compareTo(s) >= 0) 1 else 0
            return 1
        }
        val key = (i.toLong() shl 1) or (if (tight) 1L else 0L)
        memo[key]?.let { return it }
        var up = if (tight) t[i] - '0' else limit
        if (up > limit) up = limit
        var res = 0L
        for (d in 0..up) {
            if (i == 0 && d == 0) continue
            res += dfs(t, pref, i + 1, tight && d == (t[i] - '0'), memo)
        }
        memo[key] = res
        return res
    }

    fun numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long {
        this.s = s
        this.limit = limit
        return count(finish) - count(start - 1)
    }
}
