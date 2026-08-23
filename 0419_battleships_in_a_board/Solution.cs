// LeetCode 0419 - Battleships in a Board

// https://leetcode.com/problems/battleships-in-a-board/



public class Solution {

    public int CountBattleships(char[][] board) {

        int count = 0;



        for (int row = 0; row < board.Length; row++) {

            for (int col = 0; col < board[0].Length; col++) {

                if (board[row][col] != 'X') {

                    continue;

                }



                if (row > 0 && board[row - 1][col] == 'X') {

                    continue;

                }



                if (col > 0 && board[row][col - 1] == 'X') {

                    continue;

                }



                count++;

            }

        }



        return count;

    }

}
