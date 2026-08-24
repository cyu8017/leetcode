// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

export function minimumOperations(grid: any): any {
    const m = grid.length, n = grid[0].length;
    let ans = 0;
    for (let j = 0; j < n; j++) {
        for (let i = 1; i < m; i++) {
            if (grid[i][j] <= grid[i - 1][j]) {
                const need = grid[i - 1][j] + 1;
                ans += need - grid[i][j];
                grid[i][j] = need;
            }
        }
    }
    return ans;
}
