// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution {
    fun maxDistance(grid: Array<IntArray>): Int {
        val n = grid.size
        val queue = ArrayDeque<IntArray>()
        for (r in 0 until n) {
            for (c in 0 until n) {
                if (grid[r][c] == 1) queue.add(intArrayOf(r, c))
            }
        }
        if (queue.isEmpty() || queue.size == n * n) return -1
        var dist = -1
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            dist++
            repeat(queue.size) {
                val cur = queue.removeFirst()
                for (d in dirs) {
                    val nr = cur[0] + d[0]
                    val nc = cur[1] + d[1]
                    if (nr in 0 until n && nc in 0 until n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1
                        queue.add(intArrayOf(nr, nc))
                    }
                }
            }
        }
        return dist
    }
}
