// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

/**
 * @param {number[][]} board
 * @return {number[][]}
 */
var candyCrush = function(board) {
    const m = board.length, n = board[0].length;
    let stable = false;
    while (!stable) {
        stable = true;
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n - 2; j++) {
                const value = Math.abs(board[i][j]);
                if (value !== 0 && value === Math.abs(board[i][j + 1]) && value === Math.abs(board[i][j + 2])) {
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -value;
                    stable = false;
                }
            }
        }
        for (let j = 0; j < n; j++) {
            for (let i = 0; i < m - 2; i++) {
                const value = Math.abs(board[i][j]);
                if (value !== 0 && value === Math.abs(board[i + 1][j]) && value === Math.abs(board[i + 2][j])) {
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -value;
                    stable = false;
                }
            }
        }
        for (let j = 0; j < n; j++) {
            let write = m - 1;
            for (let i = m - 1; i >= 0; i--) {
                if (board[i][j] > 0) board[write--][j] = board[i][j];
            }
            for (let i = write; i >= 0; i--) board[i][j] = 0;
        }
    }
    return board;
};
