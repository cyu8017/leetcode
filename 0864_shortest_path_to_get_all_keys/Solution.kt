// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution {
    fun shortestPathAllKeys(grid: Array<String>): Int {
        var m = grid.size, n = grid[0].length
        var allKeys = 0
        var sr = 0
        var sc = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                var ch = grid[i][j]
                if (ch == '@') { sr = i; sc = j; }
                else if (ch >= 'a' && ch <= 'f') allKeys |= 1  shl  (ch - 'a')
            }
        }
        var queue = ArrayDeque<IntArray>()
        queue.offer(intArrayOf(sr, sc, 0, 0))
        var seen = HashSet<Long>()
        seen.add(encode(sr, sc, 0))
        var dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1}
        while (!queue.isEmpty()) {
            var cur = queue.poll()
            var r = cur[0]
            var c = cur[1]
            var mask = cur[2]
            var dist = cur[3]
            if (mask == allKeys) return dist
            for (k in 0 until 4) {
                var nr = r + dr[k]
                var nc = c + dc[k]
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue
                var cell = grid[nr][nc]
                var nmask = mask
                if (cell >= 'a' && cell <= 'f') nmask |= 1  shl  (cell - 'a')
                if (cell >= 'A' && cell <= 'F' && (mask & (1  shl  (cell - 'A'))) == 0) continue
                if (seen.add(encode(nr, nc, nmask))) queue.offer(intArrayOf(nr, nc, nmask, dist + 1))
            }
        }
        return -1
    }

    private fun encode(r: Int, c: Int, mask: Int): Long {
        return (r  shl  20) | (c  shl  10) | mask
    }
}
