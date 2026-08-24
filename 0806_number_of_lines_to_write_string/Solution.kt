// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution {
    fun numberOfLines(widths: IntArray, s: String): IntArray {
        var lines = 1
        var width = 0
        for (ch in s.toCharArray()) {
            var w = widths[ch - 'a']
            if (width + w > 100) {
                lines++
                width = w
            } else {
                width += w
            }
        }
        return intArrayOf(lines, width)
    }
}
