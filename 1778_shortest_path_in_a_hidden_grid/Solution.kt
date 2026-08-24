// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

class Solution {
    fun findShortestPath(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var sr = 0
        var sc = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == -1) {
                    sr = i
                    sc = j
                }
            }
        }
        val dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
        val dist = Array(m) { IntArray(n) { -1 } }
        val queue = ArrayDeque<Pair<Int, Int>>()
        dist[sr][sc] = 0
        queue.addLast(sr to sc)
        while (queue.isNotEmpty()) {
            val (r, c) = queue.removeFirst()
            if (grid[r][c] == 2) {
                return dist[r][c]
            }
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr in 0 until m && nc in 0 until n && grid[nr][nc] != 0 && dist[nr][nc] < 0) {
                    dist[nr][nc] = dist[r][c] + 1
                    queue.addLast(nr to nc)
                }
            }
        }
        return -1
    }
}
