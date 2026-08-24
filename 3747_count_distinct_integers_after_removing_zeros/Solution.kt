// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count_distinct_integers_after_removing_zeros/

class Solution {
    private lateinit var s: String
    private var m = 0
    private lateinit var f: Array<Array<Array<LongArray>>>

    fun countDistinct(n: Long): Long {
        s = n.toString()
        m = s.length
        f = Array(20) { Array(2) { Array(2) { LongArray(2) { -1 } } } }
        return dfs(0, 0, 1, 1)
    }

    private fun dfs(i: Int, zero: Int, lead: Int, limit: Int): Long {
        if (i == m) return if (zero == 0 && lead == 0) 1 else 0
        if (limit == 0 && f[i][zero][lead][limit] != -1L) return f[i][zero][lead][limit]
        val up = if (limit == 1) s[i] - '0' else 9
        var ans = 0L
        for (d in 0..up) {
            var nxtZero = zero
            if (d == 0 && lead == 0) nxtZero = 1
            val nxtLead = if (lead == 1 && d == 0) 1 else 0
            val nxtLimit = if (limit == 1 && d == up) 1 else 0
            ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit)
        }
        if (limit == 0) f[i][zero][lead][limit] = ans
        return ans
    }
}
