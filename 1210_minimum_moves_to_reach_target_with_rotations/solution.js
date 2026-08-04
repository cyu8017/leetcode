// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumMoves = function(grid) {
    const n = grid.length;
    const start = '0,0,0', target = (n - 1) + ',' + (n - 2) + ',0';
    const queue = [[0, 0, 0, 0]];
    const seen = new Set([start]);
    let qi = 0;
    while (qi < queue.length) {
        const [r, c, orient, moves] = queue[qi++];
        if (r + ',' + c + ',' + orient === target) return moves;
        const nxt = [];
        if (orient === 0) {
            if (c + 2 < n && grid[r][c + 2] === 0) nxt.push([r, c + 1, 0]);
            if (r + 1 < n && grid[r + 1][c] === 0 && grid[r + 1][c + 1] === 0) {
                nxt.push([r + 1, c, 0], [r, c, 1]);
            }
        } else {
            if (r + 2 < n && grid[r + 2][c] === 0) nxt.push([r + 1, c, 1]);
            if (c + 1 < n && grid[r][c + 1] === 0 && grid[r + 1][c + 1] === 0) {
                nxt.push([r, c + 1, 1], [r, c, 0]);
            }
        }
        for (const [nr, nc, no] of nxt) {
            const key = nr + ',' + nc + ',' + no;
            if (!seen.has(key)) {
                seen.add(key);
                queue.push([nr, nc, no, moves + 1]);
            }
        }
    }
    return -1;
};
