// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

var countGoodArrays = function(n, m, k) {
    const mod = 1000000007;
    const modPow = (a, e) => {
        let r = 1n;
        let base = BigInt(((a % mod) + mod) % mod);
        let exp = BigInt(e);
        const MOD = BigInt(mod);
        while (exp > 0n) {
            if (exp & 1n) r = (r * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return Number(r);
    };
    const comb = (nn, kk) => {
        if (kk < 0 || kk > nn) return 0;
        let num = 1, den = 1;
        for (let i = 0; i < kk; i++) {
            num = (num * (nn - i)) % mod;
            den = (den * (i + 1)) % mod;
        }
        return (num * modPow(den, mod - 2)) % mod;
    };
    return (comb(n - 1, k) * m % mod * modPow(m - 1, n - 1 - k) % mod);
};
