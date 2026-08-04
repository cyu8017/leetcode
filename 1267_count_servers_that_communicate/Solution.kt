// LeetCode 1267 - Count Servers That Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

class Solution {
    fun countServers(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val rows = IntArray(m)
        val cols = IntArray(n)
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 1) {
                    rows[r]++
                    cols[c]++
                }
            }
        }
        var count = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1)) count++
            }
        }
        return count
    }
}
