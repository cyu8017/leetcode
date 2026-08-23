// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

/**
 * @param {character[][]} board
 * @return {number}
 */
var numRookCaptures = function(board) {
    const m = board.length, n = board[0].length;
    let r = -1, c = -1;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (board[i][j] === 'R') { r = i; c = j; }
    if (r < 0) return 0;
    let ans = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    for (const [dr, dc] of dirs) {
        let i = r + dr, j = c + dc;
        while (i >= 0 && i < m && j >= 0 && j < n) {
            if (board[i][j] === 'B') break;
            if (board[i][j] === 'p') { ans++; break; }
            i += dr; j += dc;
        }
    }
    return ans;
};
