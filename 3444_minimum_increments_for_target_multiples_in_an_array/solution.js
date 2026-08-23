// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

var minimumIncrements = function(nums, target) {
    const gcd = (a, b) => { while (b) { const t = a % b; a = b; b = t; } return a; };
    const lcm = (a, b) => a / gcd(a, b) * b;
    const m = target.length;
    const N = 1 << m;
    const inf = 1e18;
    let dp = new Array(N).fill(inf);
    dp[0] = 0;
    for (const x of nums) {
        const ndp = dp.slice();
        for (let mask = 0; mask < N; mask++) {
            for (let sub = 1; sub < N; sub++) {
                let L = 1;
                let ok = true;
                for (let i = 0; i < m; i++) {
                    if (sub & (1 << i)) {
                        L = lcm(L, target[i]);
                        if (L > 1000000000) { ok = false; break; }
                    }
                }
                if (!ok) continue;
                const cost = (L - x % L) % L;
                const nmask = mask | sub;
                if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost;
            }
        }
        dp = ndp;
    }
    return dp[N - 1];
};
