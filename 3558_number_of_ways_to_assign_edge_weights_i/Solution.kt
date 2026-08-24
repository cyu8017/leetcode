// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution {
    fun assignEdgeWeights(edges: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val n = edges.size + 1
        val g = Array(n + 1) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        return pow2(dfs(1, 0, g) - 1, mod)
    }

    fun dfs(i: Int, fa: Int, g: Array<ArrayList<Int>>): Int {
        var res = 0
        for (j in g[i]) if (j != fa) res = maxOf(res, dfs(j, i, g) + 1)
        return res
    }

    fun pow2(exp0: Int, mod: Int): Int {
        var exp = exp0
        var a = 2L
        var res = 1L
        while (exp > 0) {
            if ((exp and 1) != 0) res = res * a % mod
            a = a * a % mod
            exp = exp shr 1
        }
        return res.toInt()
    }
}
