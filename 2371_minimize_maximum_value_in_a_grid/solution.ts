// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

export function minScore(grid: number[][]): number[][] {
    const m = grid.length, n = grid[0].length;
    const arr = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            arr.push([grid[i][j], i, j]);
    arr.sort((a, b) => a[0] - b[0]);
    const rowMax = Array(m).fill(0), colMax = Array(n).fill(0);
    const ans = Array.from({ length: m }, () => Array(n).fill(0));
    for (const cel of arr) {
        const val = Math.max(rowMax[cel[1]], colMax[cel[2]]) + 1;
        ans[cel[1]][cel[2]] = val;
        rowMax[cel[1]] = val;
        colMax[cel[2]] = val;
    }
    return ans;
}
