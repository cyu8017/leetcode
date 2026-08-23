// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

var countOfArrays = function(n, m, k) {
    const mod = 1000000007;
    const even = Math.floor(m / 2), odd = m - even;
    const dp = Array.from({length: n + 1}, () =>
        Array.from({length: k + 1}, () => [0, 0]));
    dp[1][0][0] = odd;
    dp[1][0][1] = even;
    for (let i = 1; i < n; i++) {
        for (let j = 0; j <= k; j++) {
            dp[i + 1][j][0] = (dp[i + 1][j][0] + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod) % mod;
            dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod;
            if (j < k) {
                dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod) % mod;
            }
        }
    }
    return (dp[n][k][0] + dp[n][k][1]) % mod;
};
