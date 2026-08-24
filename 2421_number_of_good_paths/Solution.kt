// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

class Solution {
    private lateinit var parent: IntArray
    private lateinit var size: IntArray

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    fun numberOfGoodPaths(vals: IntArray, edges: Array<IntArray>): Int {
        val n = vals.size
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        parent = IntArray(n) { it }
        size = IntArray(n) { 1 }
        val nodes = Array(n) { it }
        nodes.sortWith(compareBy { vals[it] })
        var ans = n
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && vals[nodes[j]] == vals[nodes[i]]) j++
            for (k in i until j) {
                val u = nodes[k]
                for (v in g[u]) {
                    if (vals[v] <= vals[u]) {
                        val ru = find(u)
                        val rv = find(v)
                        if (ru != rv) {
                            parent[ru] = rv
                            size[rv] += size[ru]
                        }
                    }
                }
            }
            val freq = HashMap<Int, Int>()
            for (k in i until j) {
                val r = find(nodes[k])
                freq[r] = freq.getOrDefault(r, 0) + 1
            }
            for (c in freq.values) ans += c * (c - 1) / 2
            i = j
        }
        return ans
    }
}
