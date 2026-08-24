// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

import java.util.ArrayDeque

class Solution {
    fun minDays(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        if (islands(grid, m, n) != 1) return 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 0
                    if (islands(grid, m, n) != 1) {
                        grid[r][c] = 1
                        return 1
                    }
                    grid[r][c] = 1
                }
            }
        }
        return 2
    }

    private fun islands(grid: Array<IntArray>, m: Int, n: Int): Int {
        val seen = Array(m) { BooleanArray(n) }
        var count = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 1 && !seen[r][c]) {
                    count++
                    val stack = ArrayDeque<IntArray>()
                    stack.push(intArrayOf(r, c))
                    seen[r][c] = true
                    while (stack.isNotEmpty()) {
                        val cur = stack.pop()
                        for (d in dirs) {
                            val nx = cur[0] + d[0]
                            val ny = cur[1] + d[1]
                            if (nx in 0 until m && ny in 0 until n && grid[nx][ny] == 1 && !seen[nx][ny]) {
                                seen[nx][ny] = true
                                stack.push(intArrayOf(nx, ny))
                            }
                        }
                    }
                }
            }
        }
        return count
    }
}
