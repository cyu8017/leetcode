// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

class Solution {
    fun treeDiameter(edges: Array<IntArray>): Int {
        if (edges.isEmpty()) return 0
        val graph = mutableMapOf<Int, MutableList<Int>>()
        for (e in edges) {
            graph.getOrPut(e[0]) { mutableListOf() }.add(e[1])
            graph.getOrPut(e[1]) { mutableListOf() }.add(e[0])
        }
        val first = farthest(edges[0][0], graph)
        return farthest(first[0], graph)[1]
    }

    private fun farthest(start: Int, graph: Map<Int, List<Int>>): IntArray {
        val q = ArrayDeque<IntArray>()
        val seen = mutableSetOf(start)
        q.add(intArrayOf(start, 0))
        var last = intArrayOf(start, 0)
        while (q.isNotEmpty()) {
            last = q.removeFirst()
            for (v in graph[last[0]].orEmpty()) {
                if (seen.add(v)) q.add(intArrayOf(v, last[1] + 1))
            }
        }
        return last
    }
}
