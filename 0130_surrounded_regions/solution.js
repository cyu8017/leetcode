// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

/**
 * @param {string[][]} board
 * @return {void}
 */
var solve = function(board) {
    if (!board.length || !board[0].length) {
        return;
    }

    const rows = board.length;
    const cols = board[0].length;
    const mark = (row, col) => {
        if (
            row < 0 ||
            row >= rows ||
            col < 0 ||
            col >= cols ||
            board[row][col] !== "O"
        ) {
            return;
        }

        board[row][col] = "E";
        mark(row + 1, col);
        mark(row - 1, col);
        mark(row, col + 1);
        mark(row, col - 1);
    };

    for (let row = 0; row < rows; row++) {
        mark(row, 0);
        mark(row, cols - 1);
    }
    for (let col = 0; col < cols; col++) {
        mark(0, col);
        mark(rows - 1, col);
    }

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (board[row][col] === "O") {
                board[row][col] = "X";
            } else if (board[row][col] === "E") {
                board[row][col] = "O";
            }
        }
    }
};