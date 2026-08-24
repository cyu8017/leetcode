// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

import java.util.ArrayDeque
import java.util.TreeSet

class Solution {
    fun getAncestors(n: Int, edges: Array<IntArray>): List<List<Int>> {
        val g = Array(n) { mutableListOf<Int>() }
        val indeg = IntArray(n)
        for (e in edges) {
            g[e[0]].add(e[1])
            indeg[e[1]]++
        }
        val anc = Array(n) { TreeSet<Int>() }
        val q = ArrayDeque<Int>()
        for (i in 0 until n) if (indeg[i] == 0) q.offer(i)
        while (q.isNotEmpty()) {
            val u = q.poll()
            for (v in g[u]) {
                anc[v].add(u)
                anc[v].addAll(anc[u])
                if (--indeg[v] == 0) q.offer(v)
            }
        }
        return List(n) { anc[it].toList() }
    }
}
