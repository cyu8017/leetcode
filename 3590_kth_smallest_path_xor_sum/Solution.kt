// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

class Solution {
    lateinit var g: Array<ArrayList<Int>>
    lateinit var xorPath: IntArray
    lateinit var vals: IntArray
    lateinit var inT: IntArray
    lateinit var outT: IntArray
    lateinit var order: ArrayList<Int>

    fun dfs(u: Int) {
        xorPath[u] = xorPath[u] xor vals[u]
        for (v in g[u]) {
            xorPath[v] = xorPath[u]
            dfs(v)
        }
    }

    fun dfs2(u: Int) {
        inT[u] = order.size
        order.add(xorPath[u])
        for (v in g[u]) dfs2(v)
        outT[u] = order.size
    }

    fun kthSmallest(par: IntArray, vals: IntArray, queries: Array<IntArray>): IntArray {
        val n = par.size
        this.vals = vals
        g = Array(n) { ArrayList() }
        for (i in 1 until n) g[par[i]].add(i)
        xorPath = IntArray(n)
        dfs(0)
        inT = IntArray(n)
        outT = IntArray(n)
        order = ArrayList()
        dfs2(0)
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val u = queries[i][0]
            val k = queries[i][1]
            val sub = ArrayList(order.subList(inT[u], outT[u]))
            sub.sort()
            val uniq = ArrayList<Int>()
            for (x in sub) if (uniq.isEmpty() || uniq.last() != x) uniq.add(x)
            ans[i] = if (k > uniq.size) -1 else uniq[k - 1]
        }
        return ans
    }
}
