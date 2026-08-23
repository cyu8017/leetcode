// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

var countIslands = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const dirs = [-1, 0, 1, 0, -1];
    const dfs = (i, j) => {
        let s = grid[i][j];
        grid[i][j] = 0;
        for (let d = 0; d < 4; d++) {
            const x = i + dirs[d], y = j + dirs[d + 1];
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0) s += dfs(x, y);
        }
        return s;
    };
    let ans = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] > 0 && dfs(i, j) % k === 0) ans++;
    return ans;
};
