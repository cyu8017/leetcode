// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

public class Solution {
    public bool ValidTicTacToe(string[] board) {
        string flat = board[0] + board[1] + board[2];
        int xCount = 0, oCount = 0;
        foreach (char ch in flat) {
            if (ch == 'X') xCount++;
            else if (ch == 'O') oCount++;
        }
        if (oCount != xCount && oCount != xCount - 1) return false;
        bool xWin = Win(board, 'X');
        bool oWin = Win(board, 'O');
        if (xWin && oWin) return false;
        if (xWin && xCount != oCount + 1) return false;
        if (oWin && xCount != oCount) return false;
        return true;
    }

    private bool Win(string[] board, char player) {
        string target = new string(player, 3);
        foreach (string row in board) if (row == target) return true;
        for (int c = 0; c < 3; c++) {
            if (board[0][c] == player && board[1][c] == player && board[2][c] == player) return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;
        return false;
    }
}
