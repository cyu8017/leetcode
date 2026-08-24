// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

class Solution {
    lateinit var inT: IntArray
    lateinit var outT: IntArray
    lateinit var dist: IntArray
    lateinit var parent: IntArray
    lateinit var bit: IntArray
    var time = 0
    var n = 0
    lateinit var g: Array<ArrayList<IntArray>>

    fun dfs(u: Int, p: Int) {
        inT[u] = time++
        for (e in g[u]) {
            val to = e[0]
            val ww = e[1]
            if (to == p) continue
            parent[to] = u
            dist[to] = dist[u] + ww
            dfs(to, u)
        }
        outT[u] = time - 1
    }

    fun add(i0: Int, v: Int) {
        var i = i0
        while (i <= n) {
            bit[i] += v
            i += i and -i
        }
    }

    fun rangeAdd(l: Int, r: Int, v: Int) {
        add(l + 1, v)
        add(r + 2, -v)
    }

    fun point(i0: Int): Int {
        var i = i0 + 1
        var s = 0
        while (i > 0) {
            s += bit[i]
            i -= i and -i
        }
        return s
    }

    fun treeQueries(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        this.n = n
        g = Array(n + 1) { ArrayList() }
        val weight = HashMap<Long, Int>()
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val ww = e[2]
            g[u].add(intArrayOf(v, ww))
            g[v].add(intArrayOf(u, ww))
            val a = minOf(u, v)
            val b = maxOf(u, v)
            weight[((a.toLong() shl 32) or b.toLong())] = ww
        }
        inT = IntArray(n + 1)
        outT = IntArray(n + 1)
        dist = IntArray(n + 1)
        parent = IntArray(n + 1)
        time = 0
        dfs(1, 0)
        bit = IntArray(n + 2)
        for (i in 1..n) rangeAdd(inT[i], inT[i], dist[i])
        val ans = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1) {
                val u = q[1]
                val v = q[2]
                val nw = q[3]
                val a = minOf(u, v)
                val b = maxOf(u, v)
                val key = (a.toLong() shl 32) or b.toLong()
                val ow = weight[key]!!
                val delta = nw - ow
                weight[key] = nw
                val child = if (parent[u] == v) u else v
                rangeAdd(inT[child], outT[child], delta)
            } else {
                ans.add(point(inT[q[1]]))
            }
        }
        return ans.toIntArray()
    }
}
