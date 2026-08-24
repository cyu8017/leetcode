// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

class Solution {
    fun reachableNodes(edges: Array<IntArray>, maxMoves: Int, n: Int): Int {
        val graph = Array(n) { HashMap<Int, Int>() }
        for (e in edges) {
            graph[e[0]][e[1]] = e[2]
            graph[e[1]][e[0]] = e[2]
        }
        val pq = java.util.PriorityQueue<IntArray>(compareByDescending { it[0] })
        pq.offer(intArrayOf(maxMoves, 0))
        val seen = HashMap<Int, Int>()
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val moves = cur[0]
            val node = cur[1]
            if (seen.containsKey(node)) continue
            seen[node] = moves
            for ((nei, w) in graph[node]) {
                val remain = moves - w - 1
                if (!seen.containsKey(nei) && remain >= 0) {
                    pq.offer(intArrayOf(remain, nei))
                }
            }
        }
        var ans = seen.size
        for (e in edges) {
            val left = seen.getOrDefault(e[0], 0)
            val right = seen.getOrDefault(e[1], 0)
            ans += minOf(e[2], left + right)
        }
        return ans
    }
}
