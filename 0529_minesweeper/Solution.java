// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

class Solution {
    private static final int[][] DIRECTIONS = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1},
    };

    public Object[] updateBoard(Object[] board, int[] click) {
        int rows = board.length;
        int cols = ((String[]) board[0]).length;
        char[][] grid = new char[rows][cols];
        for (int row = 0; row < rows; row++) {
            String[] sourceRow = (String[]) board[row];
            for (int col = 0; col < cols; col++) {
                grid[row][col] = sourceRow[col].charAt(0);
            }
        }

        int row = click[0];
        int col = click[1];
        if (grid[row][col] == 'M') {
            grid[row][col] = 'X';
            return toObjectBoard(grid);
        }

        reveal(grid, row, col);
        return toObjectBoard(grid);
    }

    private void reveal(char[][] board, int row, int col) {
        int rows = board.length;
        int cols = board[0].length;
        if (row < 0 || row >= rows || col < 0 || col >= cols || board[row][col] != 'E') {
            return;
        }

        int mines = countMines(board, row, col);
        board[row][col] = mines == 0 ? 'B' : (char) ('0' + mines);
        if (mines == 0) {
            for (int[] direction : DIRECTIONS) {
                reveal(board, row + direction[0], col + direction[1]);
            }
        }
    }

    private int countMines(char[][] board, int row, int col) {
        int total = 0;
        for (int[] direction : DIRECTIONS) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];
            if (nextRow >= 0 && nextRow < board.length
                    && nextCol >= 0 && nextCol < board[0].length
                    && board[nextRow][nextCol] == 'M') {
                total++;
            }
        }
        return total;
    }

    private Object[] toObjectBoard(char[][] board) {
        Object[] result = new Object[board.length];
        for (int row = 0; row < board.length; row++) {
            String[] line = new String[board[row].length];
            for (int col = 0; col < board[row].length; col++) {
                line[col] = String.valueOf(board[row][col]);
            }
            result[row] = line;
        }
        return result;
    }
}
