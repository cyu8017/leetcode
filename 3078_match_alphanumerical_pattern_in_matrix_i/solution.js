// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

/**
 * @param {number[][]} board
 * @param {string[]} pattern
 * @return {number[]}
 */
var findPattern = function(board, pattern) {
    const m = board.length, n = board[0].length;
    const r = pattern.length, c = pattern[0].length;
    const check = (i, j) => {
        const d1 = new Array(26).fill(0), d2 = new Array(10).fill(0);
        for (let a = 0; a < r; a++) {
            for (let b = 0; b < c; b++) {
                const x = i + a, y = j + b;
                const ch = pattern[a][b];
                if (ch >= '0' && ch <= '9') {
                    if (ch.charCodeAt(0) - 48 !== board[x][y]) return false;
                } else {
                    const v = ch.charCodeAt(0) - 97;
                    if (d1[v] > 0 && d1[v] - 1 !== board[x][y]) return false;
                    if (d2[board[x][y]] > 0 && d2[board[x][y]] - 1 !== v) return false;
                    d1[v] = board[x][y] + 1;
                    d2[board[x][y]] = v + 1;
                }
            }
        }
        return true;
    };
    for (let i = 0; i < m - r + 1; i++)
        for (let j = 0; j < n - c + 1; j++)
            if (check(i, j)) return [i, j];
    return [-1, -1];
};
