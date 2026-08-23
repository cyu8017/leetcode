// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

public class Solution {
    private static readonly (int dr, int dc)[] Directions = {
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    };

    public string[][] UpdateBoard(string[][] board, int[] click) {
        int row = click[0];
        int col = click[1];
        if (board[row][col] == "M") {
            board[row][col] = "X";
            return board;
        }
        Reveal(board, row, col);
        return board;
    }

    private static void Reveal(string[][] board, int row, int col) {
        if (row < 0 || row >= board.Length || col < 0 || col >= board[0].Length || board[row][col] != "E") {
            return;
        }
        int mines = CountMines(board, row, col);
        board[row][col] = mines == 0 ? "B" : mines.ToString();
        if (mines == 0) {
            foreach ((int dr, int dc) in Directions) {
                Reveal(board, row + dr, col + dc);
            }
        }
    }

    private static int CountMines(string[][] board, int row, int col) {
        int total = 0;
        foreach ((int dr, int dc) in Directions) {
            int nextRow = row + dr;
            int nextCol = col + dc;
            if (nextRow >= 0 && nextRow < board.Length
                    && nextCol >= 0 && nextCol < board[0].Length
                    && board[nextRow][nextCol] == "M") {
                total++;
            }
        }
        return total;
    }
}
