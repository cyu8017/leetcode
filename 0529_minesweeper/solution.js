// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

class Solution {
    updateBoard(board, click) {
        const rows = board.length;
        const cols = board[0].length;
        const [row, col] = click;
        const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

        if (board[row][col] === "M") {
            board[row][col] = "X";
            return board;
        }

        const countMines = (r, c) => {
            let total = 0;
            for (const [dr, dc] of directions) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] === "M") total += 1;
            }
            return total;
        };

        const reveal = (r, c) => {
            if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] !== "E") return;
            const mines = countMines(r, c);
            board[r][c] = mines === 0 ? "B" : String(mines);
            if (mines === 0) {
                for (const [dr, dc] of directions) reveal(r + dr, c + dc);
            }
        };

        reveal(row, col);
        return board;
    }
}

module.exports = { Solution };
