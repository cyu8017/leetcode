// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

export function distinctSequences(n: number): number {
    const mod = 1000000007;
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const dp = Array.from({ length: n + 1 }, () =>
        Array.from({ length: 7 }, () => Array(7).fill(0))
    );
    for (let a = 1; a <= 6; ++a) dp[1][a][0] = 1;
    for (let i = 2; i <= n; ++i) {
        for (let prev = 1; prev <= 6; ++prev) {
            for (let pprev = 0; pprev <= 6; ++pprev) {
                if (dp[i - 1][prev][pprev] === 0) continue;
                for (let cur = 1; cur <= 6; ++cur) {
                    if (cur === prev || cur === pprev || gcd(cur, prev) !== 1) continue;
                    dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod;
                }
            }
        }
    }
    let ans = 0;
    for (let a = 1; a <= 6; ++a)
        for (let b = 0; b <= 6; ++b)
            ans = (ans + dp[n][a][b]) % mod;
    return ans;
}
