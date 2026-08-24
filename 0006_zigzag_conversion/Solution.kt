// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

class Solution {
    fun convert(s: String, numRows: Int): String {
        if (numRows == 1 || numRows >= s.length) {
            return s
        }

        val rows = Array(numRows) { StringBuilder() }
        var index = 0
        var step = 1

        for (ch in s) {
            rows[index].append(ch)
            if (index == 0) {
                step = 1
            } else if (index == numRows - 1) {
                step = -1
            }
            index += step
        }

        return rows.joinToString("") { it.toString() }
    }
}
