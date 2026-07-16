// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

export function gameOfLife(board: number[][]): void {
    const rows = board.length;
    const cols = board[0].length;
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            let liveNeighbors = 0;
            for (let dr = -1; dr <= 1; dr += 1) {
                for (let dc = -1; dc <= 1; dc += 1) {
                    if (dr === 0 && dc === 0) {
                        continue;
                    }
                    const nr = row + dr;
                    const nc = col + dc;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && (board[nr][nc] & 1)) {
                        liveNeighbors += 1;
                    }
                }
            }
            if ((board[row][col] & 1) && (liveNeighbors === 2 || liveNeighbors === 3)) {
                board[row][col] |= 2;
            } else if ((board[row][col] & 1) === 0 && liveNeighbors === 3) {
                board[row][col] |= 2;
            }
        }
    }
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            board[row][col] >>= 1;
        }
    }
}
