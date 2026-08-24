// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

class Solution {
    private var k = 0
    private lateinit var s: String
    private lateinit var memo: HashMap<String, Long>

    private fun depth(x0: Int): Int {
        var x = x0
        if (x <= 0) return 100
        var d = 0
        while (x > 1) {
            x = x.countOneBits()
            d++
        }
        return d
    }

    private fun dfs(pos: Int, tight: Int, started: Int, pc: Int): Long {
        if (pos == s.length) {
            if (started == 0) return 0
            if (pc == 1) return if (k == 1) 1 else 0
            return if (depth(pc) == k - 1) 1 else 0
        }
        val key = "$pos,$tight,$started,$pc"
        memo[key]?.let { return it }
        val up = if (tight == 1) s[pos] - '0' else 1
        var res = 0L
        for (dig in 0..up) {
            val nt = if (tight == 1 && dig == up) 1 else 0
            res += if (started == 0 && dig == 0) dfs(pos + 1, nt, 0, 0)
            else dfs(pos + 1, nt, 1, pc + dig)
        }
        memo[key] = res
        return res
    }

    fun popcountDepth(n: Long, k: Int): Long {
        this.k = k
        if (k == 0) return if (n >= 1) 1 else 0
        val sb = StringBuilder()
        var x = n
        while (x > 0) {
            sb.append(('0'.code + (x and 1).toInt()).toChar())
            x = x shr 1
        }
        s = sb.reverse().toString()
        if (s.isEmpty()) s = "0"
        memo = HashMap()
        return dfs(0, 1, 0, 0)
    }
}
