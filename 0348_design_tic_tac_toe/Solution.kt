// LeetCode 0348 - Design Tic-Tac-Toe

// https://leetcode.com/problems/design-tic-tac-toe/



class TicTacToe(private val n: Int) {

    private val rows = IntArray(n)

    private val cols = IntArray(n)

    private var diag = 0

    private var antiDiag = 0



    fun move(row: Int, col: Int, player: Int): Int {

        val add = if (player == 1) 1 else -1



        rows[row] += add

        cols[col] += add

        if (row == col) {

            diag += add

        }

        if (row + col == n - 1) {

            antiDiag += add

        }



        if (kotlin.math.abs(rows[row]) == n

            || kotlin.math.abs(cols[col]) == n

            || kotlin.math.abs(diag) == n

            || kotlin.math.abs(antiDiag) == n) {

            return player

        }



        return 0

    }

}
