// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

import java.util.PriorityQueue

class Solution {
    fun maxProbability(n: Int, edges: Array<IntArray>, succProb: DoubleArray, startNode: Int, endNode: Int): Double {
        val graph = List(n) { mutableListOf<DoubleArray>() }
        for (i in edges.indices) {
            val a = edges[i][0]
            val b = edges[i][1]
            val probability = succProb[i]
            graph[a].add(doubleArrayOf(b.toDouble(), probability))
            graph[b].add(doubleArrayOf(a.toDouble(), probability))
        }
        val heap = PriorityQueue<DoubleArray>(compareByDescending { it[0] })
        val best = DoubleArray(n)
        best[startNode] = 1.0
        heap.offer(doubleArrayOf(1.0, startNode.toDouble()))
        while (heap.isNotEmpty()) {
            val current = heap.poll()
            val probability = current[0]
            val node = current[1].toInt()
            if (node == endNode) return probability
            if (probability < best[node]) continue
            for (edge in graph[node]) {
                val neighbor = edge[0].toInt()
                val candidate = probability * edge[1]
                if (candidate > best[neighbor]) {
                    best[neighbor] = candidate
                    heap.offer(doubleArrayOf(candidate, neighbor.toDouble()))
                }
            }
        }
        return 0.0
    }
}
