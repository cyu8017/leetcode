// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

import java.util.PriorityQueue
import kotlin.math.abs

class Solution {
    fun minimumEffortPath(heights: Array<IntArray>): Int {
        val m = heights.size
        val n = heights[0].size
        val dist = Array(m) { IntArray(n) { Int.MAX_VALUE } }
        dist[0][0] = 0
        val heap = PriorityQueue(compareBy<IntArray> { it[0] })
        heap.offer(intArrayOf(0, 0, 0))
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val effort = cur[0]
            val i = cur[1]
            val j = cur[2]
            if (i == m - 1 && j == n - 1) return effort
            if (effort != dist[i][j]) continue
            for (d in dirs) {
                val x = i + d[0]
                val y = j + d[1]
                if (x in 0 until m && y in 0 until n) {
                    val nd = maxOf(effort, abs(heights[i][j] - heights[x][y]))
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd
                        heap.offer(intArrayOf(nd, x, y))
                    }
                }
            }
        }
        return 0
    }
}
