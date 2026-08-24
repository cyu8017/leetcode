// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/
var modPow = function(a, b) {
        let res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    
};
var ensureInit = function() {
        if (inited) return;
        inited = true;
        f[0] = 1;
        g[0] = 1;
        for (let i = 1; i < MX; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = modPow(f[i], MOD - 2);
        }
    
};
var comb = function(n, k) {
        if (k < 0 || k > n) return 0;
        return f[n] * g[k] % MOD * g[n - k] % MOD;
    
};
var countValidSequences = function(n, k) {
        ensureInit();
        let ans = comb(n - 1, k - 1);
        if ((n + k) % 2 == 0) {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        return ans;
    
};
