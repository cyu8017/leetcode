// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

class Solution {
    fun findBall(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val ans = IntArray(n)
        for (start in 0 until n) {
            var col = start
            for (row in 0 until m) {
                val next = col + grid[row][col]
                if (next < 0 || next == n || grid[row][next] != grid[row][col]) {
                    col = -1
                    break
                }
                col = next
            }
            ans[start] = col
        }
        return ans
    }
}
