// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

class Solution {
    private var n = 0
    private lateinit var grid: Array<IntArray>
    private lateinit var memo: Array<Array<IntArray>>

    fun cherryPickup(grid: Array<IntArray>): Int {
        n = grid.size
        this.grid = grid
        memo = Array(n) { Array(n) { IntArray(n) { Int.MIN_VALUE } } }
        return maxOf(0, dp(0, 0, 0))
    }

    private fun dp(r1: Int, c1: Int, c2: Int): Int {
        val r2 = r1 + c1 - c2
        if (r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1) {
            return -1_000_000_000
        }
        if (r1 == n - 1 && c1 == n - 1) return grid[r1][c1]
        if (memo[r1][c1][c2] != Int.MIN_VALUE) return memo[r1][c1][c2]
        var cherries = grid[r1][c1]
        if (r1 != r2 || c1 != c2) cherries += grid[r2][c2]
        cherries += maxOf(
            maxOf(dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2)),
            maxOf(dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2 + 1))
        )
        memo[r1][c1][c2] = cherries
        return cherries
    }
}
