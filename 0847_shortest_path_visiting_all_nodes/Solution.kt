// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution {
    fun shortestPathLength(graph: Array<IntArray>): Int {
        var n = graph.size
        var target = (1  shl  n) - 1
        var queue = ArrayDeque<IntArray>()
        var seen = HashSet<Long>()
        for (i in 0 until n) {
            queue.offer(intArrayOf(i, 1  shl  i, 0))
            seen.add((i  shl  20) | (1  shl  i))
        }
        while (!queue.isEmpty()) {
            var cur = queue.poll()
            var node = cur[0]
            var mask = cur[1]
            var dist = cur[2]
            if (mask == target) return dist
            for (nxt in graph[node]) {
                var nmask = mask | (1  shl  nxt)
                var state = (nxt  shl  20) | nmask
                if (seen.add(state)) queue.offer(intArrayOf(nxt, nmask, dist + 1))
            }
        }
        return -1
    }
}
