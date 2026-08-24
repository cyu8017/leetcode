// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution {

    fun minimumObstacles(grid: Array<IntArray>): Int {

            var m = grid.size; var n = grid[0].size
            var dist = Array(m) { IntArray(n) }
            for (i in 0 until m) { dist[i].fill(Int.MAX_VALUE / 2) }
            dist[0][0] = 0
            var dq = ArrayDeque<Int>()
            dq.addLast(intArrayOf(0, 0))
            var dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } }
            while (!dq.isEmpty()) {
                var cur = dq.pollFirst()
                var r = cur[0]; var c = cur[1]
                for (d in dirs) {
                    var nr = r + d[0]; var nc = c + d[1]
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue
                    var nd = dist[r][c] + grid[nr][nc]
                    if (nd < dist[nr][nc]) {
                        dist[nr][nc] = nd
                        if (grid[nr][nc] == 0) dq.addFirst(intArrayOf(nr, nc))
                        else dq.addLast(intArrayOf(nr, nc))
                    }
                }
            }
            return dist[m - 1][n - 1]

    }

}
