// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

export function maxSum(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    let ans = -Infinity;
    for (let i = 0; i + 2 < m; i++) {
        for (let j = 0; j + 2 < n; j++) {
            const s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                + grid[i + 1][j + 1]
                + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
            ans = Math.max(ans, s);
        }
    }
    return ans;
}
