// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumMoves = function(grid) {
    const extras = [], zeros = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (grid[i][j] === 0) zeros.push([i, j]);
            else if (grid[i][j] > 1) {
                for (let k = 0; k < grid[i][j] - 1; k++) extras.push([i, j]);
            }
        }
    }
    if (!zeros.length) return 0;
    let best = 1 << 30;
    const dfs = (i, cost) => {
        if (cost >= best) return;
        if (i === zeros.length) {
            best = cost;
            return;
        }
        for (let j = 0; j < extras.length; j++) {
            if (extras[j][0] < 0) continue;
            const e = extras[j];
            extras[j] = [-1, e[1]];
            const d = Math.abs(e[0] - zeros[i][0]) + Math.abs(e[1] - zeros[i][1]);
            dfs(i + 1, cost + d);
            extras[j] = e;
        }
    };
    dfs(0, 0);
    return best;
};
