// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

class Solution {
    fun minimumVisitedCells(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dist = Array(m) { IntArray(n) { -1 } }
        dist[0][0] = 1
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, 0))
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val r = cur[0]
            val c = cur[1]
            if (r == m - 1 && c == n - 1) return dist[r][c]
            var nc = c + 1
            while (nc <= c + grid[r][c] && nc < n) {
                if (dist[r][nc] == -1) {
                    dist[r][nc] = dist[r][c] + 1
                    q.add(intArrayOf(r, nc))
                }
                nc += 1
            }
            var nr = r + 1
            while (nr <= r + grid[r][c] && nr < m) {
                if (dist[nr][c] == -1) {
                    dist[nr][c] = dist[r][c] + 1
                    q.add(intArrayOf(nr, c))
                }
                nr += 1
            }
        }
        return -1
    }
}
