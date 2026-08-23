// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var numDistinctIslands = function(grid) {
    if (grid === null || grid.length === 0) return 0;
    const dfs = (r, c, br, bc, path) => {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] === 0) return;
        grid[r][c] = 0;
        path.push((r - br) + ',' + (c - bc));
        dfs(r + 1, c, br, bc, path);
        dfs(r - 1, c, br, bc, path);
        dfs(r, c + 1, br, bc, path);
        dfs(r, c - 1, br, bc, path);
    };
    const shapes = new Set();
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === 1) {
                const path = [];
                dfs(i, j, i, j, path);
                shapes.add(path.join(';'));
            }
        }
    }
    return shapes.size;
};
