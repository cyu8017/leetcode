// LeetCode 0348 - Design Tic-Tac-Toe
class TicTacToe {
    constructor(n) {
        this.n = n;
        this.rows = Array(n).fill(0);
        this.cols = Array(n).fill(0);
        this.diag = 0;
        this.antiDiag = 0;
    }

    move(row, col, player) {
        const add = player === 1 ? 1 : -1;
        this.rows[row] += add;
        this.cols[col] += add;
        if (row === col) this.diag += add;
        if (row + col === this.n - 1) this.antiDiag += add;

        if (
            Math.abs(this.rows[row]) === this.n ||
            Math.abs(this.cols[col]) === this.n ||
            Math.abs(this.diag) === this.n ||
            Math.abs(this.antiDiag) === this.n
        ) {
            return player;
        }

        return 0;
    }
}

module.exports = { TicTacToe };
