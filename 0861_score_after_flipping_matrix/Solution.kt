// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

class Solution {
    fun matrixScore(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        for (row in grid) {
            if (row[0] == 0) {
                for (j in 0 until n) { row[j] ^= 1 }
            }
        }
        var ans = m * (1  shl  (n - 1))
        for (j in 1 until n) {
            var ones = 0
            for (i in 0 until m) { ones += grid[i][j] }
            ans += maxOf(ones, m - ones) * (1  shl  (n - 1 - j))
        }
        return ans
    }
}
