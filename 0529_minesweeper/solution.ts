// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

export class Solution {
    updateBoard(board: string[][], click: number[]): string[][] {
        const rows = board.length;
        const cols = board[0].length;
        const [row, col] = click;
        const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

        if (board[row][col] === "M") {
            board[row][col] = "X";
            return board;
        }

        const countMines = (r: number, c: number): number => {
            let total = 0;
            for (const [dr, dc] of directions) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] === "M") total += 1;
            }
            return total;
        };

        const reveal = (r: number, c: number): void => {
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
