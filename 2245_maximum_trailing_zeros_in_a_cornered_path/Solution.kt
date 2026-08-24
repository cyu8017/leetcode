// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution {

    private fun fact(x: Int): IntArray {

            var t = 0; var f = 0
            while (x % 2 == 0) { t++; x /= 2; }
            while (x % 5 == 0) { f++; x /= 5; }
            return intArrayOf(t, f)

    }


    fun maxTrailingZeros(grid: Array<IntArray>): Int {

            var m = grid.size; var n = grid[0].size
            var left2 = Array(m) { IntArray(n) }, left5 = Array(m) { IntArray(n) }
            var up2 = Array(m) { IntArray(n) }, up5 = Array(m) { IntArray(n) }
            for (i in 0 until m) {
                for (j in 0 until n) {
                    var p = fact(grid[i][j])
                    left2[i][j] = up2[i][j] = p[0]
                    left5[i][j] = up5[i][j] = p[1]
                    if (j > 0) {
                        left2[i][j] += left2[i][j - 1]
                        left5[i][j] += left5[i][j - 1]
                    }
                    if (i > 0) {
                        up2[i][j] += up2[i - 1][j]
                        up5[i][j] += up5[i - 1][j]
                    }
                }
            }
            var ans = 0
            for (i in 0 until m) {
                for (j in 0 until n) {
                    var cell = fact(grid[i][j])
                    var L2 = left2[i][j]; var L5 = left5[i][j]
                    var R2 = left2[i][n - 1] - left2[i][j] + cell[0]
                    var R5 = left5[i][n - 1] - left5[i][j] + cell[1]
                    var U2 = up2[i][j]; var U5 = up5[i][j]
                    var D2 = up2[m - 1][j] - up2[i][j] + cell[0]
                    var D5 = up5[m - 1][j] - up5[i][j] + cell[1]
                    var cands = {
                        { L2 + U2 - cell[0], L5 + U5 - cell[1] },
                        { L2 + D2 - cell[0], L5 + D5 - cell[1] },
                        { R2 + U2 - cell[0], R5 + U5 - cell[1] },
                        { R2 + D2 - cell[0], R5 + D5 - cell[1] },
                    }
                    for (c in cands) ans = maxOf(ans, minOf(c[0], c[1]))
                }
            }
            return ans

    }

}
