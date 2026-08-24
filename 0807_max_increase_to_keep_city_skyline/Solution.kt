// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    fun maxIncreaseKeepingSkyline(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        var rowMax = IntArray(m), colMax = IntArray(n)
        for (r in 0 until m) {
            for (c in 0 until n) {
                rowMax[r] = maxOf(rowMax[r], grid[r][c])
                colMax[c] = maxOf(colMax[c], grid[r][c])
            }
        }
        var ans = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                ans += minOf(rowMax[r], colMax[c]) - grid[r][c]
            }
        }
        return ans
    }
}
