// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

export function maximumAmount(coins: any): any {
    const m = coins.length, n = coins[0].length;
    const neg = -(1 << 30);
    const dp = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Array(3).fill(neg))
    );
    if (coins[0][0] < 0) {
        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = 0;
        dp[0][0][2] = 0;
    } else {
        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = coins[0][0];
        dp[0][0][2] = coins[0][0];
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            for (let k = 0; k < 3; k++) {
                let best = neg;
                if (i > 0) best = Math.max(best, dp[i - 1][j][k]);
                if (j > 0) best = Math.max(best, dp[i][j - 1][k]);
                if (best === neg) continue;
                if (coins[i][j] >= 0) dp[i][j][k] = best + coins[i][j];
                else dp[i][j][k] = Math.max(dp[i][j][k], best + coins[i][j]);
            }
            for (let k = 1; k < 3; k++) {
                let best = neg;
                if (i > 0) best = Math.max(best, dp[i - 1][j][k - 1]);
                if (j > 0) best = Math.max(best, dp[i][j - 1][k - 1]);
                if (best !== neg && coins[i][j] < 0)
                    dp[i][j][k] = Math.max(dp[i][j][k], best);
            }
        }
    }
    return Math.max(dp[m - 1][n - 1][0], Math.max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]));
}
