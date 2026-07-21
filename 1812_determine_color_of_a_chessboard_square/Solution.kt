// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution {
    fun squareIsWhite(coordinates: String): Boolean {
        val col = coordinates[0] - 'a' + 1
        val row = coordinates[1] - '0'
        return (col + row) % 2 == 1
    }
}
