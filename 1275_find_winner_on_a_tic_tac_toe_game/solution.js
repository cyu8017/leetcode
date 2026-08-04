// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    const board = Array.from({ length: 3 }, () => new Array(3).fill(0));
    for (let i = 0; i < moves.length; i++) {
        const [r, c] = moves[i];
        board[r][c] = i % 2 === 0 ? 1 : -1;
    }
    const lines = [];
    for (let i = 0; i < 3; i++) lines.push(board[i]);
    for (let c = 0; c < 3; c++) lines.push([board[0][c], board[1][c], board[2][c]]);
    lines.push([board[0][0], board[1][1], board[2][2]]);
    lines.push([board[0][2], board[1][1], board[2][0]]);
    for (const line of lines) {
        const sum = line[0] + line[1] + line[2];
        if (Math.abs(sum) === 3) return sum === 3 ? 'A' : 'B';
    }
    return moves.length === 9 ? 'Draw' : 'Pending';
};
