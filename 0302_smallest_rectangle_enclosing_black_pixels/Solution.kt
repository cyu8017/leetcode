// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

class Solution {
    fun minArea(image: Array<CharArray>, x: Int, y: Int): Int {
        val rows = image.size
        val cols = image[0].size

        var left = 0
        var right = y
        while (left < right) {
            val mid = (left + right) / 2
            if (columnHasBlack(image, mid, rows)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        val leftBound = left

        left = y
        right = cols - 1
        while (left < right) {
            val mid = (left + right + 1) / 2
            if (columnHasBlack(image, mid, rows)) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        val rightBound = left

        var top = 0
        var bottom = x
        while (top < bottom) {
            val mid = (top + bottom) / 2
            if (rowHasBlack(image, mid, cols)) {
                bottom = mid
            } else {
                top = mid + 1
            }
        }
        val topBound = top

        top = x
        bottom = rows - 1
        while (top < bottom) {
            val mid = (top + bottom + 1) / 2
            if (rowHasBlack(image, mid, cols)) {
                top = mid
            } else {
                bottom = mid - 1
            }
        }
        val bottomBound = top

        return (rightBound - leftBound + 1) * (bottomBound - topBound + 1)
    }

    private fun columnHasBlack(image: Array<CharArray>, col: Int, rows: Int): Boolean {
        for (row in 0 until rows) {
            if (image[row][col] == '1') {
                return true
            }
        }
        return false
    }

    private fun rowHasBlack(image: Array<CharArray>, row: Int, cols: Int): Boolean {
        for (col in 0 until cols) {
            if (image[row][col] == '1') {
                return true
            }
        }
        return false
    }
}
