// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

export function removeOnes(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const ones = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 1) ones.push([i, j]);
    if (ones.length === 0) return 0;
    let ans = m + n;
    const dfs = (idx, flips) => {
        if (flips >= ans) return;
        while (idx < ones.length && grid[ones[idx][0]][ones[idx][1]] === 0) idx++;
        if (idx === ones.length) { ans = flips; return; }
        const r = ones[idx][0], c = ones[idx][1];
        let changed = [];
        for (let j = 0; j < n; j++) if (grid[r][j] === 1) { grid[r][j] = 0; changed.push([r, j]); }
        dfs(idx + 1, flips + 1);
        for (const [x, y] of changed) grid[x][y] = 1;
        changed = [];
        for (let i = 0; i < m; i++) if (grid[i][c] === 1) { grid[i][c] = 0; changed.push([i, c]); }
        dfs(idx + 1, flips + 1);
        for (const [x, y] of changed) grid[x][y] = 1;
    };
    dfs(0, 0);
    return ans;
}
