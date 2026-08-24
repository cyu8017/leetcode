// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

import java.util.ArrayDeque

class Solution {
    fun maximumSafenessFactor(grid: MutableList<MutableList<Int>>): Int {
        val n = grid.size
        val dist = Array(n) { IntArray(n) { -1 } }
        val q = ArrayDeque<IntArray>()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0
                    q.offer(intArrayOf(i, j))
                }
            }
        }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (q.isNotEmpty()) {
            val cur = q.poll()
            val x = cur[0]
            val y = cur[1]
            for (d in dirs) {
                val ni = x + d[0]
                val nj = y + d[1]
                if (ni in 0 until n && nj in 0 until n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[x][y] + 1
                    q.offer(intArrayOf(ni, nj))
                }
            }
        }
        var lo = 0
        var hi = n * n
        var ans = 0
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (ok(dist, dirs, mid)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private fun ok(dist: Array<IntArray>, dirs: Array<IntArray>, sf: Int): Boolean {
        val n = dist.size
        if (dist[0][0] < sf) return false
        val seen = Array(n) { BooleanArray(n) }
        val st = ArrayList<IntArray>()
        st.add(intArrayOf(0, 0))
        seen[0][0] = true
        while (st.isNotEmpty()) {
            val cur = st.removeAt(st.size - 1)
            val x = cur[0]
            val y = cur[1]
            if (x == n - 1 && y == n - 1) return true
            for (d in dirs) {
                val ni = x + d[0]
                val nj = y + d[1]
                if (ni in 0 until n && nj in 0 until n && !seen[ni][nj] && dist[ni][nj] >= sf) {
                    seen[ni][nj] = true
                    st.add(intArrayOf(ni, nj))
                }
            }
        }
        return false
    }
}
