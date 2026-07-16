// LeetCode 0419 - Battleships in a Board
export function countBattleships(board: string[][]): number {
    let count = 0;
    for (let row = 0; row < board.length; row += 1) {
        for (let col = 0; col < board[0].length; col += 1) {
            if (board[row][col] !== "X") continue;
            if (row > 0 && board[row - 1][col] === "X") continue;
            if (col > 0 && board[row][col - 1] === "X") continue;
            count += 1;
        }
    }
    return count;
}
