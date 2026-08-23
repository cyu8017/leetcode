// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

var maxScore = function(a, b) {
    const neg = -(1n << 62n);
    const dp = [0n, neg, neg, neg, neg];
    for (const x of b) {
        for (let k = 4; k >= 1; k--) {
            if (dp[k - 1] === neg) continue;
            const v = dp[k - 1] + BigInt(a[k - 1]) * BigInt(x);
            if (v > dp[k]) dp[k] = v;
        }
    }
    return Number(dp[4]);
};
