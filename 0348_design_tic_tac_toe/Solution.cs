// LeetCode 0348 - Design Tic-Tac-Toe

// https://leetcode.com/problems/design-tic-tac-toe/



public class TicTacToe {

    private readonly int n;

    private readonly int[] rows;

    private readonly int[] cols;

    private int diag;

    private int antiDiag;



    public TicTacToe(int n) {

        this.n = n;

        rows = new int[n];

        cols = new int[n];

    }



    public int Move(int row, int col, int player) {

        int add = player == 1 ? 1 : -1;



        rows[row] += add;

        cols[col] += add;

        if (row == col) {

            diag += add;

        }

        if (row + col == n - 1) {

            antiDiag += add;

        }



        if (Math.Abs(rows[row]) == n

            || Math.Abs(cols[col]) == n

            || Math.Abs(diag) == n

            || Math.Abs(antiDiag) == n) {

            return player;

        }



        return 0;

    }

}
