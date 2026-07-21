// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

class Solution {
    fun getBiggestThree(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val s1 = Array(m + 1) { IntArray(n + 2) }
        val s2 = Array(m + 1) { IntArray(n + 2) }
        for (i in 1..m) {
            for (j in 1..n) {
                val value = grid[i - 1][j - 1]
                s1[i][j] = s1[i - 1][j - 1] + value
                s2[i][j] = s2[i - 1][j + 1] + value
            }
        }
        val rhombusSums = HashSet<Int>()
        for (i in 1..m) {
            for (j in 1..n) {
                val value = grid[i - 1][j - 1]
                val limit = minOf(i - 1, m - i, j - 1, n - j)
                rhombusSums.add(value)
                for (k in 1..limit) {
                    val a = s1[i + k][j] - s1[i][j - k]
                    val b = s1[i][j + k] - s1[i - k][j]
                    val c = s2[i][j - k] - s2[i - k][j]
                    val d = s2[i + k][j] - s2[i][j + k]
                    rhombusSums.add(a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1])
                }
            }
        }
        return rhombusSums.sortedDescending().take(3).toIntArray()
    }
}
