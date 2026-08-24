// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

class Solution {
    fun findPattern(board: Array<IntArray>, pattern: Array<String>): IntArray {
        val m = board.size
        val n = board[0].size
        val r = pattern.size
        val c = pattern[0].length
        for (i in 0 until m - r + 1) {
            for (j in 0 until n - c + 1) {
                if (check(board, pattern, i, j, r, c)) return intArrayOf(i, j)
            }
        }
        return intArrayOf(-1, -1)
    }

    private fun check(board: Array<IntArray>, pattern: Array<String>, i: Int, j: Int, r: Int, c: Int): Boolean {
        val d1 = IntArray(26)
        val d2 = IntArray(10)
        for (a in 0 until r) {
            for (b in 0 until c) {
                val x = i + a
                val y = j + b
                val ch = pattern[a][b]
                if (ch in '0'..'9') {
                    if (ch - '0' != board[x][y]) return false
                } else {
                    val v = ch - 'a'
                    if (d1[v] > 0 && d1[v] - 1 != board[x][y]) return false
                    if (d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v) return false
                    d1[v] = board[x][y] + 1
                    d2[board[x][y]] = v + 1
                }
            }
        }
        return true
    }
}
