// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKSubsequencesWithMaxBeauty = function(s, k) {
    const MOD = 1000000007n;
    const freq = Array(26).fill(0);
    for (const ch of s) freq[ch.charCodeAt(0) - 97]++;
    const vals = freq.filter((f) => f > 0).sort((a, b) => b - a);
    if (vals.length < k) return 0;
    const threshold = vals[k - 1];
    let need = 0, avail = 0;
    let prod = 1n;
    for (const v of vals) {
        if (v > threshold) {
            prod = (prod * BigInt(v)) % MOD;
            need++;
        } else if (v === threshold) avail++;
    }
    const remain = k - need;
    const modPow = (a, b) => {
        let res = 1n;
        a %= MOD;
        while (b > 0n) {
            if (b & 1n) res = (res * a) % MOD;
            a = (a * a) % MOD;
            b >>= 1n;
        }
        return res;
    };
    const comb = (n, r) => {
        if (r < 0 || r > n) return 0n;
        let num = 1n, den = 1n;
        for (let i = 0; i < r; i++) {
            num = (num * BigInt(n - i)) % MOD;
            den = (den * BigInt(i + 1)) % MOD;
        }
        return (num * modPow(den, MOD - 2n)) % MOD;
    };
    prod = (prod * comb(avail, remain)) % MOD;
    for (let i = 0; i < remain; i++) prod = (prod * BigInt(threshold)) % MOD;
    return Number(prod);
};
