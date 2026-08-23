// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

function entry3603(i, j) { return (i + 1) * (j + 1); }
var minCost = function(m, n, waitCost) {
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const dp = Array.from({length: m}, () => new Array(n).fill(INF));
    dp[0][0] = entry3603(0, 0);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            if (i > 0) {
                let cand = dp[i - 1][j] + entry3603(i, j);
                if (!(i - 1 === 0 && j === 0)) cand += waitCost[i - 1][j];
                dp[i][j] = Math.min(dp[i][j], cand);
            }
            if (j > 0) {
                let cand = dp[i][j - 1] + entry3603(i, j);
                if (!(i === 0 && j - 1 === 0)) cand += waitCost[i][j - 1];
                dp[i][j] = Math.min(dp[i][j], cand);
            }
        }
    }
    return dp[m - 1][n - 1];
};
