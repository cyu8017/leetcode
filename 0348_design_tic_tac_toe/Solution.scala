// LeetCode 0348 - Design Tic-Tac-Toe

// https://leetcode.com/problems/design-tic-tac-toe/



class TicTacToe(n: Int) {

  private val rows = Array.fill(n)(0)

  private val cols = Array.fill(n)(0)

  private var diag = 0

  private var antiDiag = 0



  def move(row: Int, col: Int, player: Int): Int = {

    val add = if (player == 1) 1 else -1



    rows(row) += add

    cols(col) += add

    if (row == col) {

      diag += add

    }

    if (row + col == n - 1) {

      antiDiag += add

    }



    if (math.abs(rows(row)) == n

      || math.abs(cols(col)) == n

      || math.abs(diag) == n

      || math.abs(antiDiag) == n) {

      player

    } else {

      0

    }

  }

}
