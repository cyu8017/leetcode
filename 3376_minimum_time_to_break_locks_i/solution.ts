// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

function bitsOnes(x: any): any {
    let c = 0;
    while (x > 0) { c += x & 1; x >>= 1; }
    return c;
}export function findMinimumTime(strength: any, k: any): any {
    const n = strength.length;
    const inf = 1000000000;
    const N = 1 << n;
    const dp = new Array(N).fill(inf);
    dp[0] = 0;
    for (let mask = 0; mask < N; mask++) {
        if (dp[mask] === inf) continue;
        const opened = bitsOnes(mask);
        const x = 1 + opened * k;
        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) !== 0) continue;
            const t = Math.floor((strength[i] + x - 1) / x);
            const nmask = mask | (1 << i);
            if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
        }
    }
    return dp[N - 1];
}
