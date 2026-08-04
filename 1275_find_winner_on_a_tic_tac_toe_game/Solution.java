// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

import java.util.*;

class Solution {
    public String tictactoe(int[][] moves) {
        int[][] board = new int[3][3];
        for (int i = 0; i < moves.length; i++) {
            board[moves[i][0]][moves[i][1]] = i % 2 == 0 ? 1 : -1;
        }
        List<int[]> lines = new ArrayList<>();
        for (int i = 0; i < 3; i++) lines.add(board[i]);
        for (int c = 0; c < 3; c++) lines.add(new int[] {board[0][c], board[1][c], board[2][c]});
        lines.add(new int[] {board[0][0], board[1][1], board[2][2]});
        lines.add(new int[] {board[0][2], board[1][1], board[2][0]});
        for (int[] line : lines) {
            int sum = line[0] + line[1] + line[2];
            if (Math.abs(sum) == 3) return sum == 3 ? "A" : "B";
        }
        return moves.length == 9 ? "Draw" : "Pending";
    }
}
