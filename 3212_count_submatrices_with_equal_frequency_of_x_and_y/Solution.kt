// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution {
    fun numberOfSubmatrices(grid: Array<CharArray>): Int {
        var m = grid.size
        var n = grid[0].size
        int[][][] s = IntArray(m + 1)[][]
        for (i in 0 ..m) {
            s[i] = IntArray(n + 1)[]
            for (j in 0 ..n) { s[i][j] = IntArray(2) }
        }
        var ans = 0
        for (i in 1 ..m) {
            for (j in 1 ..n) {
                s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
                if (grid[i - 1][j - 1] == 'X') s[i][j][0]++
                s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
                if (grid[i - 1][j - 1] == 'Y') s[i][j][1]++
                if (s[i][j][0] > 0 && s[i][j][0] == s[i][j][1]) ans++
            }
        }
        return ans
    }
}
