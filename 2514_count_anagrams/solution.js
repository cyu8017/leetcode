// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

/**
 * @param {string} s
 * @return {number}
 */
var countAnagrams = function(s) {
    const MOD = 1000000007;
    const modPow = (a, e) => {
        let res = 1;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    };
    const words = s.trim() === '' ? [] : s.trim().split(/\s+/);
    let maxN = 0;
    for (const w of words) if (w.length > maxN) maxN = w.length;
    const fact = Array(maxN + 1), invFact = Array(maxN + 1);
    fact[0] = 1;
    for (let i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[maxN] = modPow(fact[maxN], MOD - 2);
    for (let i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    let ans = 1;
    for (const word of words) {
        const cnt = Array(26).fill(0);
        for (let i = 0; i < word.length; i++) cnt[word.charCodeAt(i) - 97]++;
        let cur = fact[word.length];
        for (const c of cnt) cur = cur * invFact[c] % MOD;
        ans = ans * cur % MOD;
    }
    return ans;
};
