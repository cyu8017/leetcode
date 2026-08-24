// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

export function distinctSubseqII(s: string): number {
    const MOD = 1000000007;
    const last = new Array(26).fill(-1);
    const n = s.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        dp[i + 1] = (dp[i] * 2) % MOD;
        if (last[c] >= 0) dp[i + 1] = (dp[i + 1] - dp[last[c]] + MOD) % MOD;
        last[c] = i;
    }
    return (dp[n] - 1 + MOD) % MOD;
}
