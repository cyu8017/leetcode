// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

export function maxIncreaseKeepingSkyline(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const rowMax = new Array(m).fill(0);
    const colMax = new Array(n).fill(0);
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            rowMax[r] = Math.max(rowMax[r], grid[r][c]);
            colMax[c] = Math.max(colMax[c], grid[r][c]);
        }
    }
    let ans = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            ans += Math.min(rowMax[r], colMax[c]) - grid[r][c];
        }
    }
    return ans;
}
