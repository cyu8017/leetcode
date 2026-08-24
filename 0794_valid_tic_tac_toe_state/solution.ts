// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

export function validTicTacToe(board: string[]): boolean {
    let x = 0, o = 0;
    for (const row of board) {
        for (const ch of row) {
            if (ch === 'X') x++;
            else if (ch === 'O') o++;
        }
    }
    if (o > x || x - o > 1) return false;
    const win = (player) => {
        for (let i = 0; i < 3; i++) {
            if (board[i][0] === player && board[i][1] === player && board[i][2] === player) return true;
            if (board[0][i] === player && board[1][i] === player && board[2][i] === player) return true;
        }
        if (board[0][0] === player && board[1][1] === player && board[2][2] === player) return true;
        if (board[0][2] === player && board[1][1] === player && board[2][0] === player) return true;
        return false;
    };
    const xWin = win('X');
    const oWin = win('O');
    if (xWin && oWin) return false;
    if (xWin && x !== o + 1) return false;
    if (oWin && x !== o) return false;
    return true;
}
