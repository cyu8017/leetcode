// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

class Solution {
    fun baseUnitConversions(conversions: Array<IntArray>): IntArray {
        val mod = 1_000_000_007
        val n = conversions.size + 1
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in conversions) g[e[0]].add(intArrayOf(e[1], e[2]))
        val ans = IntArray(n)
        dfs(0, 1, g, ans, mod)
        return ans
    }

    fun dfs(s: Int, mul: Int, g: Array<ArrayList<IntArray>>, ans: IntArray, mod: Int) {
        ans[s] = mul
        for (e in g[s]) dfs(e[0], ((1L * mul * e[1]) % mod).toInt(), g, ans, mod)
    }
}
