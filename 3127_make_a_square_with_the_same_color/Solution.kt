// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution {
    fun canMakeSquare(grid: Array<CharArray>): Boolean {
        var dirs = { 0, 0, 1, 1, 0 }
        for (i in 0 until 2) {
            for (j in 0 until 2) {
                var cnt1 = 0
                var cnt2 = 0
                for (k in 0 until 4) {
                    var x = i + dirs[k]
                    var y = j + dirs[k + 1]
                    if (grid[x][y] == 'W') cnt1++
                    else cnt2++
                }
                if (cnt1 != cnt2) return true
            }
        }
        return false
    }
}
