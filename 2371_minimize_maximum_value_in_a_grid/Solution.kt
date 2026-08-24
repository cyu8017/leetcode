// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

class Solution {
    fun minScore(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val arr = Array(m * n) { IntArray(3) }
        var idx = 0
        for (i in 0 until m) for (j in 0 until n) {
            arr[idx++] = intArrayOf(grid[i][j], i, j)
        }
        arr.sortBy { it[0] }
        val rowMax = IntArray(m)
        val colMax = IntArray(n)
        val ans = Array(m) { IntArray(n) }
        for (cel in arr) {
            val value = maxOf(rowMax[cel[1]], colMax[cel[2]]) + 1
            ans[cel[1]][cel[2]] = value
            rowMax[cel[1]] = value
            colMax[cel[2]] = value
        }
        return ans
    }
}
