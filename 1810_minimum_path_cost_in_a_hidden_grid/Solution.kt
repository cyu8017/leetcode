// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

import java.util.PriorityQueue

class Solution {
    fun findShortestPath(grid: Array<IntArray>, r1: Int, c1: Int, r2: Int, c2: Int): Int {
        if (r1 == r2 && c1 == c2) return 0
        val m = grid.size
        val n = grid[0].size
        val dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
        val dist = Array(m) { IntArray(n) { Int.MAX_VALUE } }
        val heap = PriorityQueue<IntArray>(compareBy { it[0] })
        dist[r1][c1] = 0
        heap.offer(intArrayOf(0, r1, c1))

        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val d = cur[0]
            val r = cur[1]
            val c = cur[2]
            if (r == r2 && c == c2) return d
            if (d > dist[r][c]) continue
            for (dir in dirs) {
                val nr = r + dir[0]
                val nc = c + dir[1]
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0) continue
                val nd = d + grid[nr][nc]
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd
                    heap.offer(intArrayOf(nd, nr, nc))
                }
            }
        }
        return -1
    }
}
