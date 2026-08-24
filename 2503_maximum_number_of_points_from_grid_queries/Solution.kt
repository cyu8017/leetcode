// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

import java.util.PriorityQueue

class Solution {
    fun maxPoints(grid: Array<IntArray>, queries: IntArray): IntArray {
        val m = grid.size
        val n = grid[0].size
        val order = Array(queries.size) { it }
        order.sortWith(compareBy { queries[it] })
        val ans = IntArray(queries.size)
        val visited = Array(m) { BooleanArray(n) }
        val pq = PriorityQueue(compareBy<IntArray> { it[0] })
        pq.offer(intArrayOf(grid[0][0], 0, 0))
        visited[0][0] = true
        var points = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for (qi in order) {
            val q = queries[qi]
            while (pq.isNotEmpty() && pq.peek()[0] < q) {
                val cell = pq.poll()
                val r = cell[1]
                val c = cell[2]
                points++
                for (d in dirs) {
                    val nr = r + d[0]
                    val nc = c + d[1]
                    if (nr in 0 until m && nc in 0 until n && !visited[nr][nc]) {
                        visited[nr][nc] = true
                        pq.offer(intArrayOf(grid[nr][nc], nr, nc))
                    }
                }
            }
            ans[qi] = points
        }
        return ans
    }
}
