// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution {
    public boolean validTicTacToe(String[] board) {
        int x = 0, o = 0;
        for (String row : board) {
            for (char ch : row.toCharArray()) {
                if (ch == 'X') x++;
                else if (ch == 'O') o++;
            }
        }
        if (o > x || x - o > 1) return false;
        boolean xWin = win(board, 'X');
        boolean oWin = win(board, 'O');
        if (xWin && oWin) return false;
        if (xWin && x != o + 1) return false;
        if (oWin && x != o) return false;
        return true;
    }

    private boolean win(String[] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i].charAt(0) == player && board[i].charAt(1) == player && board[i].charAt(2) == player)
                return true;
            if (board[0].charAt(i) == player && board[1].charAt(i) == player && board[2].charAt(i) == player)
                return true;
        }
        if (board[0].charAt(0) == player && board[1].charAt(1) == player && board[2].charAt(2) == player)
            return true;
        if (board[0].charAt(2) == player && board[1].charAt(1) == player && board[2].charAt(0) == player)
            return true;
        return false;
    }
}
