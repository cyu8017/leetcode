// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution {
    fun countSubmatrices(grid: Array<IntArray>, k: Int): Int {
        var n = grid.size
        var m = grid[0].size
        var ans = 0
        var s = IntArray(n + 1)[]
        for (i in 0 until = n) { s[i] = IntArray(m + 1) }
        for (i in 0 until n) {
            for (j in 0 until m) {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]
                if (s[i + 1][j + 1] <= k) ans++
            }
        }
        return ans
    }
}
