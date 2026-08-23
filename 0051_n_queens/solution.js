// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const result = [];
    const cols = new Set();
    const diag1 = new Set();
    const diag2 = new Set();
    const board = Array.from({ length: n }, () => '.'.repeat(n));

    function backtrack(row) {
        if (row === n) {
            result.push(board.slice());
            return;
        }

        for (let col = 0; col < n; col++) {
            if (cols.has(col) || diag1.has(row + col) || diag2.has(row - col)) {
                continue;
            }

            cols.add(col);
            diag1.add(row + col);
            diag2.add(row - col);

            const rowChars = board[row].split('');
            rowChars[col] = 'Q';
            board[row] = rowChars.join('');

            backtrack(row + 1);

            cols.delete(col);
            diag1.delete(row + col);
            diag2.delete(row - col);
            board[row] = '.'.repeat(n);
        }
    }

    backtrack(0);
    return result;
};
