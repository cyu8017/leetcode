// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        var s = 0L
        for (row in grid) for (x in row) s += x
        if (s % 2 != 0L) return false
        val m = grid.size
        val n = grid[0].size
        var pre = 0L
        for (i in 0 until m) {
            for (x in grid[i]) pre += x
            if (pre * 2 == s && i + 1 < m) return true
        }
        pre = 0
        for (j in 0 until n) {
            for (i in 0 until m) pre += grid[i][j]
            if (pre * 2 == s && j + 1 < n) return true
        }
        return false
    }
}
