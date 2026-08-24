// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution {
    fun minimumOperationsToWriteY(grid: Array<IntArray>): Int {
        val n = grid.size
        val cnt1 = IntArray(3)
        val cnt2 = IntArray(3)
        for (i in 0 until n) {
            for (j in 0 until n) {
                val x = grid[i][j]
                val a = i == j && i <= n / 2
                val b = i + j == n - 1 && i <= n / 2
                val c = j == n / 2 && i >= n / 2
                if (a || b || c) cnt1[x]++ else cnt2[x]++
            }
        }
        var ans = n * n
        for (i in 0 until 3) {
            for (j in 0 until 3) {
                if (i != j) ans = minOf(ans, n * n - cnt1[i] - cnt2[j])
            }
        }
        return ans
    }
}
