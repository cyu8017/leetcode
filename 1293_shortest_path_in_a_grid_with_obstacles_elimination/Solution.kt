// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution {
    fun shortestPath(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        if (k >= m + n - 2) return m + n - 2
        val queue = ArrayDeque<IntArray>()
        val best = mutableMapOf<Long, Int>()
        queue.add(intArrayOf(0, 0, k, 0))
        best[key(0, 0)] = k
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur[0] == m - 1 && cur[1] == n - 1) return cur[3]
            for (d in dirs) {
                val nr = cur[0] + d[0]
                val nc = cur[1] + d[1]
                if (nr !in 0 until m || nc !in 0 until n) continue
                val nxt = cur[2] - grid[nr][nc]
                if (nxt < 0) continue
                val cell = key(nr, nc)
                if (best.containsKey(cell) && nxt <= best[cell]!!) continue
                best[cell] = nxt
                queue.add(intArrayOf(nr, nc, nxt, cur[3] + 1))
            }
        }
        return -1
    }

    private fun key(r: Int, c: Int): Long = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
}
