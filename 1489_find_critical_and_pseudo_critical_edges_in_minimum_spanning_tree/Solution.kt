// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class Solution {
    fun findCriticalAndPseudoCriticalEdges(n: Int, edges: Array<IntArray>): List<List<Int>> {
        val es = edges.mapIndexed { i, e -> intArrayOf(e[2], e[0], e[1], i) }
            .sortedWith(compareBy { it[0] })

        fun mst(skip: Int = -1, force: Int = -1): Long {
            val parent = IntArray(n) { it }
            fun find(x: Int): Int {
                var cur = x
                while (cur != parent[cur]) {
                    parent[cur] = parent[parent[cur]]
                    cur = parent[cur]
                }
                return cur
            }
            var total = 0L
            var used = 0
            if (force >= 0) {
                val e = es[force]
                parent[find(e[1])] = find(e[2])
                total += e[0]
                used++
            }
            for (j in es.indices) {
                if (j == skip || j == force) continue
                val e = es[j]
                val x = find(e[1])
                val y = find(e[2])
                if (x != y) {
                    parent[x] = y
                    total += e[0]
                    used++
                }
            }
            return if (used == n - 1) total else Long.MAX_VALUE / 4
        }

        val base = mst()
        val critical = mutableListOf<Int>()
        val pseudo = mutableListOf<Int>()
        for (j in es.indices) {
            if (mst(skip = j) > base) critical.add(es[j][3])
            else if (mst(force = j) == base) pseudo.add(es[j][3])
        }
        return listOf(critical.sorted(), pseudo.sorted())
    }
}
