// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

public class Solution {
    public string Tictactoe(int[][] moves) {
        int[][] board = {
            new[] { 0, 0, 0 },
            new[] { 0, 0, 0 },
            new[] { 0, 0, 0 },
        };
        for (int i = 0; i < moves.Length; i++) {
            int r = moves[i][0], c = moves[i][1];
            board[r][c] = i % 2 == 0 ? 1 : -1;
        }
        var lines = new System.Collections.Generic.List<int[]>();
        for (int i = 0; i < 3; i++) lines.Add(board[i]);
        for (int c = 0; c < 3; c++) lines.Add(new[] { board[0][c], board[1][c], board[2][c] });
        lines.Add(new[] { board[0][0], board[1][1], board[2][2] });
        lines.Add(new[] { board[0][2], board[1][1], board[2][0] });
        foreach (var line in lines) {
            int sum = line[0] + line[1] + line[2];
            if (System.Math.Abs(sum) == 3) return sum == 3 ? "A" : "B";
        }
        return moves.Length == 9 ? "Draw" : "Pending";
    }
}
