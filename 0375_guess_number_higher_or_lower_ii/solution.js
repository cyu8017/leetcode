// LeetCode 0375 - Guess Number Higher or Lower II
var getMoneyAmount = function(n) {
    const dp = Array.from({ length: n + 2 }, () => Array(n + 2).fill(0));

    for (let length = 2; length <= n; length += 1) {
        for (let left = 1; left <= n - length + 1; left += 1) {
            const right = left + length - 1;
            dp[left][right] = Number.POSITIVE_INFINITY;
            for (let guess = left; guess < right; guess += 1) {
                const cost = guess + Math.max(dp[left][guess - 1], dp[guess + 1][right]);
                dp[left][right] = Math.min(dp[left][right], cost);
            }
        }
    }

    return dp[1][n];
};
