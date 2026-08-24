// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

export function waysToReachTarget(target: number, types: number[][]): number {
    const MOD = 1000000007;
    const dp = new Array(target + 1).fill(0);
    dp[0] = 1;
    for (const t of types) {
        const count = t[0], marks = t[1];
        for (let s = target; s >= 0; --s) {
            for (let k = 1; k <= count && s - k * marks >= 0; ++k) {
                dp[s] = (dp[s] + dp[s - k * marks]) % MOD;
            }
        }
    }
    return dp[target];
}
