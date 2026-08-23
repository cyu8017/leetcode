// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

function BIT(n) {
    this.n = n;
    this.c = new Array(n + 1).fill(0);
}
BIT.prototype.update = function(x, delta) {
    for (; x <= this.n; x += x & -x) this.c[x] += delta;
};
BIT.prototype.query = function(x) {
    let s = 0;
    for (; x > 0; x -= x & -x) s += this.c[x];
    return s;
};

/**
 * @param {number[]} perm
 * @return {number}
 */
var getPermutationIndex = function(perm) {
    const MOD = 1000000007;
    const n = perm.length;
    const tree = new BIT(n + 1);
    const f = new Array(n);
    f[0] = 1;
    for (let i = 1; i < n; i++) f[i] = f[i - 1] * i % MOD;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const x = perm[i];
        const cnt = x - 1 - tree.query(x);
        ans = (ans + cnt * f[n - 1 - i]) % MOD;
        tree.update(x, 1);
    }
    return ans;
};
