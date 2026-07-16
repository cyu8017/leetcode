// LeetCode 0419 - Battleships in a Board

// https://leetcode.com/problems/battleships-in-a-board/



class Solution {

    fun countBattleships(board: Array<CharArray>): Int {

        var count = 0



        for (row in board.indices) {

            for (col in board[0].indices) {

                if (board[row][col] != 'X') {

                    continue

                }



                if (row > 0 && board[row - 1][col] == 'X') {

                    continue

                }



                if (col > 0 && board[row][col - 1] == 'X') {

                    continue

                }



                count++

            }

        }



        return count

    }

}
