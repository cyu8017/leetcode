// LeetCode 0419 - Battleships in a Board

// https://leetcode.com/problems/battleships-in-a-board/



object Solution {

  def countBattleships(board: Array[Array[Char]]): Int = {

    var count = 0



    for (row <- board.indices) {

      for (col <- board(0).indices) {

        if (board(row)(col) != 'X') {

          // skip water

        } else if (row > 0 && board(row - 1)(col) == 'X') {

          // part of vertical ship

        } else if (col > 0 && board(row)(col - 1) == 'X') {

          // part of horizontal ship

        } else {

          count += 1

        }

      }

    }



    count

  }

}
