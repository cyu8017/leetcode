// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

class Solution {
    fun largest1BorderedSquare(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val left = Array(m) { IntArray(n) }
        val up = Array(m) { IntArray(n) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] != 0) {
                    left[r][c] = 1 + if (c > 0) left[r][c - 1] else 0
                    up[r][c] = 1 + if (r > 0) up[r - 1][c] else 0
                }
            }
        }
        var best = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 0) continue
                val limit = minOf(left[r][c], up[r][c])
                for (size in limit downTo 1) {
                    if (left[r - size + 1][c] >= size && up[r][c - size + 1] >= size) {
                        best = maxOf(best, size)
                        break
                    }
                }
            }
        }
        return best * best
    }
}
