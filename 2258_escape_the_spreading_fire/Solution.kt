// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

class Solution {

    fun maximumMinutes(grid: Array<IntArray>): Int {

            var m = grid.size; var n = grid[0].size
            var inf = 1_000_000_000
            var fire = Array(m) { IntArray(n) }
            for (i in 0 until m) { fire[i].fill(inf) }
            var q = ArrayDeque<Int>()
            for (i in 0 until m) { run { var j = 0 } j < n; while (j++)
                    if (grid[i][j] == 1) {
                        fire[i][j] = 0) { ); q.offer(intArrayOf(i, j } }
                    }
            var dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } }
            while (!q.isEmpty()) {
                var cur = q.poll()
                var r = cur[0]; var c = cur[1]
                for (d in dirs) {
                    var nr = r + d[0]; var nc = c + d[1]
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf)
                        continue
                    fire[nr][nc] = fire[r][c] + 1
                    q.offer(intArrayOf(nr, nc))
                }
            }
            var lo = 0; var hi = m * n + 10; var ans = -1
            while (lo <= hi) {
                var mid = (lo + hi) / 2
                if (can(grid, fire, mid, dirs, inf)) {
                    ans = mid
                    lo = mid + 1
                } else hi = mid - 1
            }
            if (ans >= m * n) return inf
            return ans

    }


    private fun can(grid: Array<IntArray>, fire: Array<IntArray>, wait: Int, dirs: Array<IntArray>, inf: Int): Boolean {

            var m = grid.size; var n = grid[0].size
            if (wait >= fire[0][0]) return false
            var vis = Array(m) { BooleanArray(n) }
            var qq = ArrayDeque<Int>()
            qq.offer(intArrayOf(0, 0, wait))
            vis[0][0] = true
            while (!qq.isEmpty()) {
                var cur = qq.poll()
                var r = cur[0]; var c = cur[1]; var t = cur[2]
                for (d in dirs) {
                    var nr = r + d[0]; var nc = c + d[1]; var nt = t + 1
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc])
                        continue
                    if (nr == m - 1 && nc == n - 1) {
                        if (nt <= fire[nr][nc]) return true
                        continue
                    }
                    if (nt >= fire[nr][nc]) continue
                    vis[nr][nc] = true
                    qq.offer(intArrayOf(nr, nc, nt))
                }
            }
            return false

    }

}
