// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

function MinHeap(cmp) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
MinHeap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MinHeap.prototype._down = function(i) {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MinHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MinHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MinHeap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumProduct = function(nums, k) {
    const MOD = 1000000007;
    const h = new MinHeap();
    for (const x of nums) h.push(x);
    for (let i = 0; i < k; i++) {
        const x = h.pop();
        h.push(x + 1);
    }
    let ans = 1;
    while (h.size()) ans = ans * h.pop() % MOD;
    return ans;
};
