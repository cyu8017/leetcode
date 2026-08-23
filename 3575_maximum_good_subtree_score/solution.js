// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

var goodSubtreeSum = function(vals, par) {
    const MOD = 1000000007;
    const n = vals.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[par[i]].push(i);
    let ans = 0;
    function digitMask(x) {
        const v = x;
        let mask = 0;
        if (x === 0) return [1, 1, 0];
        while (x > 0) {
            const d = x % 10;
            if ((mask & (1 << d)) !== 0) return [0, 0, 0];
            mask |= 1 << d;
            x = Math.floor(x / 10);
        }
        return [mask, 1, v];
    }
    function dfs(u) {
        let dp = new Map();
        dp.set(0, 0);
        const dm = digitMask(vals[u]);
        if (dm[1] === 1) dp.set(dm[0], dm[2]);
        for (const c of g[u]) {
            const child = dfs(c);
            const ndp = new Map();
            for (const [k1, v1] of dp) {
                for (const [k2, v2] of child) {
                    if ((k1 & k2) === 0) {
                        const nm = k1 | k2;
                        ndp.set(nm, Math.max(ndp.get(nm) || 0, v1 + v2));
                    }
                }
            }
            for (const [k, v] of dp) ndp.set(k, Math.max(ndp.get(k) || 0, v));
            for (const [k, v] of child) ndp.set(k, Math.max(ndp.get(k) || 0, v));
            dp = ndp;
        }
        let best = 0;
        for (const s of dp.values()) best = Math.max(best, s);
        ans = (ans + best) % MOD;
        return dp;
    }
    dfs(0);
    return ans;
};
