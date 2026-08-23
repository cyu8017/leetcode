// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

var findMaxFish = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dfs = (r, c) => {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] === 0) return 0;
        const fish = grid[r][c];
        grid[r][c] = 0;
        return fish + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1);
    };
    let best = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] > 0) best = Math.max(best, dfs(i, j));
    return best;
};
