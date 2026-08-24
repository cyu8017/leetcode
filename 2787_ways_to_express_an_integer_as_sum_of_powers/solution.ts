// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

export function numberOfWays(n: number, x: number): number {
    const MOD = 1000000007;
    const powers = [];
    for (let i = 1; ; i++) {
        let p = 1;
        for (let j = 0; j < x; j++) {
            p *= i;
            if (p > n) break;
        }
        if (p > n) break;
        powers.push(p);
    }
    const dp = Array(n + 1).fill(0);
    dp[0] = 1;
    for (const p of powers) {
        for (let s = n; s >= p; s--) dp[s] = (dp[s] + dp[s - p]) % MOD;
    }
    return dp[n];
}
