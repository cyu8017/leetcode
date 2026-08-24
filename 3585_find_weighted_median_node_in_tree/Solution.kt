// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

import java.util.ArrayDeque

class Solution {
    fun findMedian(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        val ans = IntArray(queries.size)
        for (qi in queries.indices) {
            val u = queries[qi][0]
            val v = queries[qi][1]
            val parent = IntArray(n) { -2 }
            val pw = IntArray(n)
            parent[u] = -1
            val q = ArrayDeque<Int>()
            q.add(u)
            while (q.isNotEmpty()) {
                val x = q.poll()
                if (x == v) break
                for (e in g[x]) {
                    if (parent[e[0]] == -2) {
                        parent[e[0]] = x
                        pw[e[0]] = e[1]
                        q.add(e[0])
                    }
                }
            }
            val nodes = ArrayList<Int>()
            nodes.add(v)
            val weights = ArrayList<Int>()
            var cur = v
            while (cur != u) {
                weights.add(pw[cur])
                cur = parent[cur]
                nodes.add(cur)
            }
            nodes.reverse()
            weights.reverse()
            var total = 0
            for (w in weights) total += w
            val need = (total + 1) / 2
            var sum = 0
            var med = u
            for (i in weights.indices) {
                sum += weights[i]
                med = nodes[i + 1]
                if (sum >= need) break
            }
            ans[qi] = med
        }
        return ans
    }
}
