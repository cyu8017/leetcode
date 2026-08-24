// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

import java.util.ArrayDeque

class Solution {
    fun getFood(grid: Array<CharArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        val queue = ArrayDeque<IntArray>()
        val seen = Array(rows) { BooleanArray(cols) }
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (grid[r][c] == '*') {
                    queue.offer(intArrayOf(r, c, 0))
                    seen[r][c] = true
                }
            }
        }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val entry = queue.poll()
            val r = entry[0]
            val c = entry[1]
            val d = entry[2]
            if (grid[r][c] == '#') {
                return d
            }
            for (dir in dirs) {
                val nr = r + dir[0]
                val nc = c + dir[1]
                if (nr in 0 until rows && nc in 0 until cols && !seen[nr][nc] && grid[nr][nc] != 'X') {
                    seen[nr][nc] = true
                    queue.offer(intArrayOf(nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
