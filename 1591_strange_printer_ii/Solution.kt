// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

import java.util.ArrayDeque

class Solution {
    fun isPrintable(targetGrid: Array<IntArray>): Boolean {
        val colors = HashSet<Int>()
        val bounds = HashMap<Int, IntArray>()
        for (r in targetGrid.indices) {
            for (col in targetGrid[r].indices) {
                val c = targetGrid[r][col]
                colors.add(c)
                val b = bounds[c]
                if (b == null) {
                    bounds[c] = intArrayOf(r, col, r, col)
                } else {
                    b[0] = minOf(b[0], r)
                    b[1] = minOf(b[1], col)
                    b[2] = maxOf(b[2], r)
                    b[3] = maxOf(b[3], col)
                }
            }
        }
        val graph = HashMap<Int, HashSet<Int>>()
        val indegree = HashMap<Int, Int>()
        for (c in colors) {
            graph[c] = HashSet()
            indegree[c] = 0
        }
        for ((c, b) in bounds) {
            for (r in b[0]..b[2]) {
                for (col in b[1]..b[3]) {
                    val other = targetGrid[r][col]
                    if (other != c && graph[c]!!.add(other)) {
                        indegree[other] = indegree[other]!! + 1
                    }
                }
            }
        }
        val queue = ArrayDeque<Int>()
        for (c in colors) {
            if (indegree[c] == 0) queue.add(c)
        }
        var seen = 0
        while (queue.isNotEmpty()) {
            val c = queue.poll()
            seen++
            for (nxt in graph[c]!!) {
                indegree[nxt] = indegree[nxt]!! - 1
                if (indegree[nxt] == 0) queue.add(nxt)
            }
        }
        return seen == colors.size
    }
}
