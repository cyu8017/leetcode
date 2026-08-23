// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

function bitsOnes(x) {
    let c = 0;
    while (x > 0) { c += x & 1; x >>= 1; }
    return c;
}
var findMinimumTime = function(strength) {
    const n = strength.length;
    const N = 1 << n;
    const inf = 1e18;
    const dp = new Array(N).fill(inf);
    dp[0] = 0;
    const k = 1;
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
};
