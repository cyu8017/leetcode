// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution {
    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        val n = grid.size
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1
        val queue = ArrayDeque<IntArray>()
        queue.add(intArrayOf(0, 0, 1))
        grid[0][0] = 1
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val r = cur[0]
            val c = cur[1]
            val dist = cur[2]
            if (r == n - 1 && c == n - 1) return dist
            for (dr in -1..1) {
                for (dc in -1..1) {
                    if (dr == 0 && dc == 0) continue
                    val nr = r + dr
                    val nc = c + dc
                    if (nr in 0 until n && nc in 0 until n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1
                        queue.add(intArrayOf(nr, nc, dist + 1))
                    }
                }
            }
        }
        return -1
    }
}
