// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

export function numTilings(n: number): number {
    const MOD = 1000000007;
    if (n === 1) return 1;
    if (n === 2) return 2;
    const dp = new Array(n + 1).fill(0);
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 5;
    for (let i = 4; i <= n; i++) dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD;
    return dp[n];
}
