// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var getMaximumGold = function(grid) {
    const rows = grid.length, cols = grid[0].length;
    const dfs = (r, c) => {
        const gold = grid[r][c];
        grid[r][c] = 0;
        let best = 0;
        for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc]) {
                best = Math.max(best, dfs(nr, nc));
            }
        }
        grid[r][c] = gold;
        return gold + best;
    };
    let ans = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c]) ans = Math.max(ans, dfs(r, c));
        }
    }
    return ans;
};
