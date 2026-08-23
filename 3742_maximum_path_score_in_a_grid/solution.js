// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum_path_score_in_a_grid/

var maxPathScore = function(grid, k) {
    const INF = 1 << 30;
    const m = grid.length, n = grid[0].length;
    const f = Array.from({length: m}, () =>
        Array.from({length: n}, () => new Array(k + 1).fill(-1)));
    const dfs = (i, j, kk) => {
        if (i < 0 || j < 0 || kk < 0) return -INF;
        if (i === 0 && j === 0) return 0;
        if (f[i][j][kk] !== -1) return f[i][j][kk];
        let res = grid[i][j];
        let nk = kk;
        if (grid[i][j] !== 0) nk--;
        const a = dfs(i - 1, j, nk);
        const b = dfs(i, j - 1, nk);
        res += Math.max(a, b);
        return f[i][j][kk] = res;
    };
    const ans = dfs(m - 1, n - 1, k);
    return ans < 0 ? -1 : ans;
};
