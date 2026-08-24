// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution {
    fun minimumTime(grid: Array<IntArray>): Int {
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1
        var m = grid.size
        var n = grid[0].size
        var dist = Array(m) { IntArray(n) }
        var i: Int = 0
while (i < m) {

            for (j in 0 until n) { dist[i][j] = 1  shl  30 }
        var h = PriorityQueue((a, b) -> (a[0]).compareTo(b[0]))
        h.offer(intArrayOf(0, 0, 0))
        dist[0][0] = 0
        var dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
        while (!h.isEmpty()) {
            var cur = h.poll()
            var t = cur[0]
            var r = cur[1]
            var c = cur[2]
            if (r == m - 1 && c == n - 1) return t
            if (t > dist[r][c]) continue
            for (d in dirs) {
                var nr = r + d[0]
                var nc = c + d[1]
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue
                var nt = t + 1
                if (nt < grid[nr][nc]) {
                    var wait = grid[nr][nc] - nt
                    if (wait % 2 == 1) { wait = wait + 1 }
                    nt += wait
                }
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt
                    h.offer(intArrayOf(nt, nr, nc))
                }
            }
        }
        return -1
    }
}
i = i + 1
}
