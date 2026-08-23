// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

var maxIncreasingCells = function(mat) {
    const m = mat.length, n = mat[0].length;
    const cells = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            cells.push([mat[i][j], i, j]);
    cells.sort((a, b) => a[0] - b[0]);
    const rowMax = new Array(m).fill(0), colMax = new Array(n).fill(0);
    const dp = Array.from({ length: m }, () => new Array(n).fill(0));
    let ans = 0;
    for (let i = 0; i < cells.length; ) {
        let j = i;
        while (j < cells.length && cells[j][0] === cells[i][0]) j++;
        const buf = [];
        for (let k = i; k < j; k++) {
            const r = cells[k][1], c = cells[k][2];
            const best = Math.max(rowMax[r], colMax[c]);
            dp[r][c] = best + 1;
            ans = Math.max(ans, dp[r][c]);
            buf.push([r, c, dp[r][c]]);
        }
        for (const [r, c, v] of buf) {
            rowMax[r] = Math.max(rowMax[r], v);
            colMax[c] = Math.max(colMax[c], v);
        }
        i = j;
    }
    return ans;
};
