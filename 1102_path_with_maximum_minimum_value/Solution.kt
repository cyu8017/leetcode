// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

import java.util.PriorityQueue

class Solution {
    fun maximumMinimumPath(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val heap = PriorityQueue<IntArray>(compareBy { it[0] })
        heap.offer(intArrayOf(-grid[0][0], 0, 0))
        val seen = Array(m) { BooleanArray(n) }
        seen[0][0] = true
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val `val` = cur[0]
            val r = cur[1]
            val c = cur[2]
            if (r == m - 1 && c == n - 1) return -`val`
            for ((dr, dc) in arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
                val nr = r + dr
                val nc = c + dc
                if (nr in 0 until m && nc in 0 until n && !seen[nr][nc]) {
                    seen[nr][nc] = true
                    heap.offer(intArrayOf(maxOf(`val`, -grid[nr][nc]), nr, nc))
                }
            }
        }
        return grid[0][0]
    }
}
