// LeetCode 1428 - Leftmost Column With At Least A One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

interface BinaryMatrix {
    fun get(row: Int, col: Int): Int
    fun dimensions(): List<Int>
}

class Solution {
    fun leftMostColumnWithOne(binaryMatrix: BinaryMatrix): Int {
        val dims = binaryMatrix.dimensions()
        val rows = dims[0]
        val cols = dims[1]
        var row = 0
        var col = cols - 1
        var answer = -1
        while (row < rows && col >= 0) {
            if (binaryMatrix.get(row, col) == 1) {
                answer = col
                col--
            } else {
                row++
            }
        }
        return answer
    }
}
