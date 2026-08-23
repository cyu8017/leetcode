// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

var magicalSum = function(m, k, nums) {
    const N = 31, MOD = 1000000007;
    const f = new Array(N).fill(0), g = new Array(N).fill(0);
    let inited = false;
    function qpow(a, kk) {
        let res = 1n;
        let ba = BigInt(a), bk = BigInt(kk), mod = BigInt(MOD);
        while (bk > 0n) {
            if (bk & 1n) res = res * ba % mod;
            ba = ba * ba % mod;
            bk >>= 1n;
        }
        return Number(res);
    }
    function initFact() {
        if (inited) return;
        f[0] = g[0] = 1;
        for (let i = 1; i < N; i++) {
            f[i] = Number(BigInt(f[i - 1]) * BigInt(i) % BigInt(MOD));
            g[i] = qpow(f[i], MOD - 2);
        }
        inited = true;
    }
    function comb(mm, nn) {
        if (nn < 0 || nn > mm) return 0;
        return Number(BigInt(f[mm]) * BigInt(g[nn]) % BigInt(MOD) * BigInt(g[mm - nn]) % BigInt(MOD));
    }
    initFact();
    const n = nums.length;
    const dp = Array.from({length: n + 1}, () =>
        Array.from({length: m + 1}, () =>
            Array.from({length: k + 1}, () => new Array(N).fill(-1))));
    function dfs(i, j, kk, st) {
        if (kk < 0 || (i === n && j > 0)) return 0;
        if (i === n) {
            while (st > 0) { kk -= st & 1; st >>= 1; }
            return kk === 0 ? 1 : 0;
        }
        if (dp[i][j][kk][st] !== -1) return dp[i][j][kk][st];
        let res = 0;
        for (let t = 0; t <= j; t++) {
            const nt = t + st;
            const nk = kk - (nt & 1);
            const p = qpow(nums[i], t);
            const tmp = Number(BigInt(comb(j, t)) * BigInt(p) % BigInt(MOD) * BigInt(dfs(i + 1, j - t, nk, nt >> 1)) % BigInt(MOD));
            res = (res + tmp) % MOD;
        }
        return dp[i][j][kk][st] = res;
    }
    return dfs(0, m, k, 0);
};
