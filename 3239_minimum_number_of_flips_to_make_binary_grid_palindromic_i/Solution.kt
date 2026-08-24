// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution {
    fun minFlips(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        var cnt1 = 0
        var cnt2 = 0
        for (var row : grid) {
            for (j in 0 until n / 2) {
                if (row[j] != row[n - j - 1]) cnt1++
            }
        }
        for (j in 0 until n) {
            for (i in 0 until m / 2) {
                if (grid[i][j] != grid[m - i - 1][j]) cnt2++
            }
        }
        return minOf(cnt1, cnt2)
    }
}
