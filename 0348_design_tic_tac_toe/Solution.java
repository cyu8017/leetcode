// LeetCode 0348 - Design Tic-Tac-Toe

// https://leetcode.com/problems/design-tic-tac-toe/



class TicTacToe {

    private final int n;

    private final int[] rows;

    private final int[] cols;

    private int diag;

    private int antiDiag;



    public TicTacToe(int n) {

        this.n = n;

        this.rows = new int[n];

        this.cols = new int[n];

    }



    public int move(int row, int col, int player) {

        int add = player == 1 ? 1 : -1;



        rows[row] += add;

        cols[col] += add;

        if (row == col) {

            diag += add;

        }

        if (row + col == n - 1) {

            antiDiag += add;

        }



        if (Math.abs(rows[row]) == n

            || Math.abs(cols[col]) == n

            || Math.abs(diag) == n

            || Math.abs(antiDiag) == n) {

            return player;

        }



        return 0;

    }

}
