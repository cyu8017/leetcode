// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

class Solution {
    private val DIRS = arrayOf(
        intArrayOf(1, 2), intArrayOf(1, -2), intArrayOf(-1, 2), intArrayOf(-1, -2),
        intArrayOf(2, 1), intArrayOf(2, -1), intArrayOf(-2, 1), intArrayOf(-2, -1)
    )

    private fun knightDist(x: Int, y: Int, pts: Array<IntArray>): IntArray {
        val np = pts.size
        val ans = IntArray(np) { -1 }
        val vis = Array(50) { BooleanArray(50) }
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(x, y, 0))
        vis[x][y] = true
        val need = HashMap<Long, MutableList<Int>>()
        for (i in 0 until np) {
            val key = (pts[i][0].toLong() shl 32) or (pts[i][1].toLong() and 0xffffffffL)
            need.getOrPut(key) { ArrayList() }.add(i)
        }
        var found = 0
        while (q.isNotEmpty() && found < np) {
            val cur = q.removeFirst()
            val key = (cur[0].toLong() shl 32) or (cur[1].toLong() and 0xffffffffL)
            val idxs = need[key]
            if (idxs != null) {
                for (i in idxs) {
                    if (ans[i] == -1) {
                        ans[i] = cur[2]
                        found++
                    }
                }
            }
            for (d in DIRS) {
                val nx = cur[0] + d[0]
                val ny = cur[1] + d[1]
                if (nx !in 0 until 50 || ny !in 0 until 50 || vis[nx][ny]) continue
                vis[nx][ny] = true
                q.add(intArrayOf(nx, ny, cur[2] + 1))
            }
        }
        return ans
    }

    fun maxMoves(kx: Int, ky: Int, positions: Array<IntArray>): Int {
        val n = positions.size
        val pts = Array(n + 1) { IntArray(2) }
        pts[0][0] = kx
        pts[0][1] = ky
        for (i in 0 until n) {
            pts[i + 1][0] = positions[i][0]
            pts[i + 1][1] = positions[i][1]
        }
        val dist = Array(n + 1) { IntArray(0) }
        for (i in 0..n) {
            dist[i] = knightDist(pts[i][0], pts[i][1], pts)
        }
        val N = 1 shl n
        val memo = Array(N) { IntArray(n + 1) { -1 } }
        return dfs(0, 0, 0, n, N, dist, memo)
    }

    private fun dfs(
        mask: Int,
        cur: Int,
        turn: Int,
        n: Int,
        N: Int,
        dist: Array<IntArray>,
        memo: Array<IntArray>
    ): Int {
        if (mask == N - 1) return 0
        if (memo[mask][cur] != -1) return memo[mask][cur]
        var best = if (turn == 0) -(1 shl 30) else (1 shl 30)
        for (i in 0 until n) {
            if ((mask and (1 shl i)) != 0) continue
            val d = dist[cur][i + 1]
            val v = d + dfs(mask or (1 shl i), i + 1, 1 - turn, n, N, dist, memo)
            if (turn == 0) {
                if (v > best) best = v
            } else if (v < best) {
                best = v
            }
        }
        memo[mask][cur] = best
        return best
    }
}
