// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution {
    fun sortItems(n: Int, m: Int, group: IntArray, beforeItems: List<List<Int>>): IntArray {
        var groupCount = m
        val g = group.copyOf()
        for (i in 0 until n) {
            if (g[i] == -1) g[i] = groupCount++
        }
        val itemGraph = Array(n) { mutableListOf<Int>() }
        val itemIndeg = IntArray(n)
        val groupGraph = Array(groupCount) { mutableListOf<Int>() }
        val groupIndeg = IntArray(groupCount)
        val seenGroupEdge = mutableSetOf<Long>()
        for (v in 0 until n) {
            for (u in beforeItems[v]) {
                itemGraph[u].add(v)
                itemIndeg[v]++
                if (g[u] != g[v]) {
                    val key = (g[u].toLong() shl 32) or (g[v].toLong() and 0xffffffffL)
                    if (seenGroupEdge.add(key)) {
                        groupGraph[g[u]].add(g[v])
                        groupIndeg[g[v]]++
                    }
                }
            }
        }
        val items = topo(itemGraph, itemIndeg)
        val groups = topo(groupGraph, groupIndeg)
        if (items.isEmpty() || groups.isEmpty()) return intArrayOf()
        val buckets = Array(groupCount) { mutableListOf<Int>() }
        for (item in items) buckets[g[item]].add(item)
        val ans = mutableListOf<Int>()
        for (gr in groups) ans.addAll(buckets[gr])
        return ans.toIntArray()
    }

    private fun topo(graph: Array<MutableList<Int>>, indeg: IntArray): List<Int> {
        val q = ArrayDeque<Int>()
        for (i in indeg.indices) if (indeg[i] == 0) q.add(i)
        val order = mutableListOf<Int>()
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            order.add(u)
            for (v in graph[u]) if (--indeg[v] == 0) q.add(v)
        }
        return if (order.size == graph.size) order else emptyList()
    }
}
