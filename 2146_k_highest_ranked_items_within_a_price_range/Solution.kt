// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

import java.util.ArrayDeque

class Solution {
    fun highestRankedKItems(grid: Array<IntArray>, pricing: IntArray, start: IntArray, k0: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        val low = pricing[0]
        val high = pricing[1]
        val vis = Array(m) { BooleanArray(n) }
        val q = ArrayDeque<IntArray>()
        q.offer(intArrayOf(start[0], start[1], 0))
        vis[start[0]][start[1]] = true
        val cands = mutableListOf<IntArray>()
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (q.isNotEmpty()) {
            val cur = q.poll()
            val r = cur[0]
            val c = cur[1]
            val d = cur[2]
            if (grid[r][c] in low..high) cands.add(intArrayOf(d, grid[r][c], r, c))
            for (dir in dirs) {
                val nr = r + dir[0]
                val nc = c + dir[1]
                if (nr in 0 until m && nc in 0 until n && !vis[nr][nc] && grid[nr][nc] != 0) {
                    vis[nr][nc] = true
                    q.offer(intArrayOf(nr, nc, d + 1))
                }
            }
        }
        cands.sortWith(compareBy({ it[0] }, { it[1] }, { it[2] }, { it[3] }))
        val k = minOf(k0, cands.size)
        return List(k) { listOf(cands[it][2], cands[it][3]) }
    }
}
