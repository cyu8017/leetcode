// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

class Solution {
    fun findLonelyPixel(picture: Array<CharArray>): Int {
        val rows = picture.size
        val cols = picture[0].size
        val rowCounts = IntArray(rows)
        val colCounts = IntArray(cols)

        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (picture[r][c] == 'B') {
                    rowCounts[r]++
                    colCounts[c]++
                }
            }
        }

        var lonely = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (picture[r][c] == 'B' && rowCounts[r] == 1 && colCounts[c] == 1) {
                    lonely++
                }
            }
        }
        return lonely
    }
}
