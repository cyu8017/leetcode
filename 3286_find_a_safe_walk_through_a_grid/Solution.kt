// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

class Solution {
    fun findSafeWalk(grid: Array<IntArray>, health: Int): Boolean {
        var m = grid.size
        var n = grid[0].size
        var vis = Array(m) { IntArray(n) }
        for (row in vis) { row.fill(-1) }
        var qh = health - grid[0][0]
        if (qh <= 0) return false
        var q = ArrayDeque<IntArray>()
        q.offer(intArrayOf(0, 0, qh))
        vis[0][0] = qh
        var dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
        while (!q.isEmpty()) {
            var cur = q.poll()
            if (cur[0] == m - 1 && cur[1] == n - 1) return true
            for (d in dirs) {
                var nr = cur[0] + d[0]
                var nc = cur[1] + d[1]
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue
                var nh = cur[2] - grid[nr][nc]
                if (nh <= 0) continue
                if (nh > vis[nr][nc]) {
                    vis[nr][nc] = nh
                    q.offer(intArrayOf(nr, nc, nh))
                }
            }
        }
        return false
    }
}
