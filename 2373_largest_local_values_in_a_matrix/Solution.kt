// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution {
    fun largestLocal(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val ans = Array(n - 2) { IntArray(n - 2) }
        for (i in 0 until n - 2) {
            for (j in 0 until n - 2) {
                var mx = 0
                for (r in i until i + 3) for (c in j until j + 3) {
                    if (grid[r][c] > mx) mx = grid[r][c]
                }
                ans[i][j] = mx
            }
        }
        return ans
    }
}
