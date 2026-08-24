// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution {
    fun tictactoe(moves: Array<IntArray>): String {
        val board = Array(3) { IntArray(3) }
        for (i in moves.indices) {
            board[moves[i][0]][moves[i][1]] = if (i % 2 == 0) 1 else -1
        }
        val lines = mutableListOf(
            board[0], board[1], board[2],
            intArrayOf(board[0][0], board[1][0], board[2][0]),
            intArrayOf(board[0][1], board[1][1], board[2][1]),
            intArrayOf(board[0][2], board[1][2], board[2][2]),
            intArrayOf(board[0][0], board[1][1], board[2][2]),
            intArrayOf(board[0][2], board[1][1], board[2][0])
        )
        for (line in lines) {
            val sum = line[0] + line[1] + line[2]
            if (kotlin.math.abs(sum) == 3) return if (sum == 3) "A" else "B"
        }
        return if (moves.size == 9) "Draw" else "Pending"
    }
}
