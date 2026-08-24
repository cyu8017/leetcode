// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var cost: IntArray
    private lateinit var ans: LongArray

    private fun dfs(u: Int, p: Int): MutableList<Int> {
        val vals = ArrayList<Int>()
        vals.add(cost[u])
        for (v in g[u]) {
            if (v == p) continue
            vals.addAll(dfs(v, u))
        }
        vals.sort()
        if (vals.size < 3) ans[u] = 1
        else {
            val m = vals.size
            val cand1 = vals[m - 1].toLong() * vals[m - 2] * vals[m - 3]
            val cand2 = vals[0].toLong() * vals[1] * vals[m - 1]
            var best = maxOf(cand1, cand2)
            if (best < 0) best = 0
            ans[u] = best
        }
        if (vals.size <= 5) return vals
        return arrayListOf(vals[0], vals[1], vals[vals.size - 3], vals[vals.size - 2], vals[vals.size - 1])
    }

    fun placedCoins(edges: Array<IntArray>, cost: IntArray): LongArray {
        val n = cost.size
        g = Array(n) { ArrayList() }
        for (e in edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]) }
        this.cost = cost
        ans = LongArray(n)
        dfs(0, -1)
        return ans
    }
}
