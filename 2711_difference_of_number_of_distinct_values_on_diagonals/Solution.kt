// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
    fun differenceOfDistinctValues(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val ans = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                val top = HashSet<Int>()
                val bot = HashSet<Int>()
                var r = i - 1
                var c = j - 1
                while (r >= 0 && c >= 0) {
                    top.add(grid[r][c])
                    r--; c--
                }
                r = i + 1; c = j + 1
                while (r < m && c < n) {
                    bot.add(grid[r][c])
                    r++; c++
                }
                ans[i][j] = kotlin.math.abs(top.size - bot.size)
            }
        }
        return ans
    }
}
