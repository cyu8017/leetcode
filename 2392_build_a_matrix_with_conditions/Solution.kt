// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

import java.util.ArrayDeque

class Solution {
    fun buildMatrix(k: Int, rowConditions: Array<IntArray>, colConditions: Array<IntArray>): Array<IntArray> {
        val rowOrder = topo(k, rowConditions) ?: return arrayOf()
        val colOrder = topo(k, colConditions) ?: return arrayOf()
        val rowPos = IntArray(k + 1)
        val colPos = IntArray(k + 1)
        for (i in 0 until k) {
            rowPos[rowOrder[i]] = i
            colPos[colOrder[i]] = i
        }
        val ans = Array(k) { IntArray(k) }
        for (v in 1..k) ans[rowPos[v]][colPos[v]] = v
        return ans
    }

    private fun topo(k: Int, conds: Array<IntArray>): IntArray? {
        val g = Array(k + 1) { ArrayList<Int>() }
        val indeg = IntArray(k + 1)
        for (c in conds) {
            g[c[0]].add(c[1])
            indeg[c[1]]++
        }
        val q = ArrayDeque<Int>()
        for (i in 1..k) if (indeg[i] == 0) q.offer(i)
        val order = IntArray(k)
        var idx = 0
        while (q.isNotEmpty()) {
            val u = q.poll()
            order[idx++] = u
            for (v in g[u]) {
                indeg[v]--
                if (indeg[v] == 0) q.offer(v)
            }
        }
        return if (idx != k) null else order
    }
}
