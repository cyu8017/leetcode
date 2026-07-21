// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

class Solution {
    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray> {
        val m = boxGrid.size
        val n = boxGrid[0].size
        val rotated = Array(n) { CharArray(m) { '.' } }
        for (i in 0 until n) {
            for (j in 0 until m) {
                rotated[i][j] = boxGrid[m - 1 - j][i]
            }
        }
        for (col in 0 until m) {
            var row = n - 1
            for (i in n - 1 downTo 0) {
                when (rotated[i][col]) {
                    '*' -> row = i - 1
                    '#' -> {
                        rotated[i][col] = '.'
                        rotated[row][col] = '#'
                        row--
                    }
                }
            }
        }
        return rotated
    }
}
