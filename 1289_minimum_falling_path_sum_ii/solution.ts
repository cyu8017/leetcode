// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

function minFallingPathSum(grid: number[][]): number {
    let dp = grid[0].slice();
    for (let rowIndex = 1; rowIndex < grid.length; rowIndex++) {
        const row = grid[rowIndex];
        let first = 0;
        for (let i = 1; i < dp.length; i++) {
            if (dp[i] < dp[first]) first = i;
        }
        let secondValue = Infinity;
        for (let i = 0; i < dp.length; i++) {
            if (i !== first) secondValue = Math.min(secondValue, dp[i]);
        }
        if (dp.length === 1) secondValue = 0;
        dp = row.map((value, i) => value + (i === first ? secondValue : dp[first]));
    }
    return Math.min(...dp);
}
