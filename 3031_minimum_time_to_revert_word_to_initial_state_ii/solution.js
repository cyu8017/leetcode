// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Hashing {
    constructor(word, bas, mod) {
        this.mod = mod;
        const n = word.length;
        this.p = new Array(n + 1);
        this.h = new Array(n + 1);
        this.p[0] = 1n;
        this.h[0] = 0n;
        const B = BigInt(bas), M = BigInt(mod);
        for (let i = 1; i <= n; i++) {
            this.p[i] = this.p[i - 1] * B % M;
            this.h[i] = (this.h[i - 1] * B + BigInt(word.charCodeAt(i - 1) - 97)) % M;
        }
    }
    query(l, r) {
        const M = BigInt(this.mod);
        return (this.h[r] - this.h[l - 1] * this.p[r - l + 1] % M + M) % M;
    }
}
var minimumTimeToInitialState = function(word, k) {
    const hashing = new Hashing(word, 13331, 998244353);
    const n = word.length;
    for (let i = k; i < n; i += k)
        if (hashing.query(1, n - i) === hashing.query(i + 1, n)) return (i / k) | 0;
    return ((n + k - 1) / k) | 0;
};
