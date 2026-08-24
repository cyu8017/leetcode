// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

class Solution {
    companion object {
        const val MOD = 1_000_000_007
    }

    fun qpow(x0: Long, n0: Int): Long {
        var x = x0
        var n = n0
        var res = 1L
        while (n > 0) {
            if ((n and 1) != 0) res = res * x % MOD
            x = x * x % MOD
            n = n shr 1
        }
        return res
    }

    fun queryConversions(conversions: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = conversions.size + 1
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in conversions) g[e[0]].add(intArrayOf(e[1], e[2]))
        val res = IntArray(n)
        dfs(0, 1, g, res)
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            ans[i] = ((1L * res[queries[i][1]] * qpow(res[queries[i][0]].toLong(), MOD - 2)) % MOD).toInt()
        }
        return ans
    }

    fun dfs(s: Int, mul: Int, g: Array<ArrayList<IntArray>>, res: IntArray) {
        res[s] = mul
        for (e in g[s]) dfs(e[0], ((1L * mul * e[1]) % MOD).toInt(), g, res)
    }
}
