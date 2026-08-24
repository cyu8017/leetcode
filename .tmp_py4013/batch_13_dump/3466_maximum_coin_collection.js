// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

var maxCoins = function(lane1, lane2) {
    const n = lane1.length;
    const neg = Number.MIN_SAFE_INTEGER / 4;
    let dp = [[lane1[0], neg], [lane2[0], neg]];
    let ans = Math.max(dp[0][0], dp[1][0]);
    for (let i = 1; i < n; i++) {
        const ndp = [[0, 0], [0, 0]];
        ndp[0][0] = Math.max(dp[0][0], 0) + lane1[i];
        ndp[1][0] = Math.max(dp[1][0], 0) + lane2[i];
        ndp[0][1] = Math.max(dp[0][1], dp[1][0]) + lane1[i];
        ndp[1][1] = Math.max(dp[1][1], dp[0][0]) + lane2[i];
        if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
        if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
        for (let a = 0; a < 2; a++)
            for (let b = 0; b < 2; b++) {
                dp[a][b] = ndp[a][b];
                if (dp[a][b] > ans) ans = dp[a][b];
            }
    }
    return ans;
};
