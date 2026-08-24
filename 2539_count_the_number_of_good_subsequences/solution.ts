// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

export function countGoodSubsequences(s: string): number {
    const MOD = 1000000007;
    const cnt = new Array(26).fill(0);
    let maxf = 0;
    for (const c of s) {
        cnt[c.charCodeAt(0) - 97]++;
        if (cnt[c.charCodeAt(0) - 97] > maxf) maxf = cnt[c.charCodeAt(0) - 97];
    }
    const fact = new Array(maxf + 1);
    const invFact = new Array(maxf + 1);
    const modPow = (a, e) => {
        let res = 1;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    };
    fact[0] = 1;
    for (let i = 1; i <= maxf; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[maxf] = modPow(fact[maxf], MOD - 2);
    for (let i = maxf; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    const comb = (n, k) => {
        if (k < 0 || k > n) return 0;
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    };
    let ans = 0;
    for (let k = 1; k <= maxf; k++) {
        let ways = 1;
        for (let i = 0; i < 26; i++) {
            if (cnt[i] >= k) ways = ways * (1 + comb(cnt[i], k)) % MOD;
        }
        ans = (ans + ways - 1 + MOD) % MOD;
    }
    return ans;
}
