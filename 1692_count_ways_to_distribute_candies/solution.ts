// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

function waysToDistribute(n: number, k: number): number {
    const MOD = 1e9 + 7;
    const dp = Array(k + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        for (let j = Math.min(i, k); j >= 1; j--) {
            dp[j] = (dp[j - 1] + j * dp[j]) % MOD;
        }
        dp[0] = 0;
    }
    return dp[k];
}
