// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

class Solution {
    fun possibleToStamp(grid: Array<IntArray>, stampHeight: Int, stampWidth: Int): Boolean {
        var m: Int = grid.size, n = grid[0].size
        var pref: Array<IntArray> = Array(m + 1) { IntArray(n + 1) }
        for (i in 0 until m)
            for (j in 0 until n)
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j]
        var diff: Array<IntArray> = Array(m + 1) { IntArray(n + 1) }
        var i = 0
        while (i + stampHeight - 1 < m) {
            var j = 0
            while (j + stampWidth - 1 < n) {
                var sum: Int = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth]
                        - pref[i + stampHeight][j] + pref[i][j]
                if (sum == 0) {
                    diff[i][j]++
                    diff[i][j + stampWidth]--
                    diff[i + stampHeight][j]--
                    diff[i + stampHeight][j + stampWidth]++
                    j++
                }
                i++
            }
        }
        var cur: Array<IntArray> = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                var v: Int = diff[i][j]
                if (i > 0) v += cur[i - 1][j]
                if (j > 0) v += cur[i][j - 1]
                if (i > 0 && j > 0) v -= cur[i - 1][j - 1]
                cur[i][j] = v
                if (grid[i][j] == 0 && v == 0) return false
            }
        }
        return true
    }
}
