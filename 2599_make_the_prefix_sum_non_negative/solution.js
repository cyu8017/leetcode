// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

function Heap(cmp) {
    this.a = [];
    this.cmp = cmp;
}
Heap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
Heap.prototype._down = function(i) {
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
Heap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
Heap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
Heap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums
 * @return {number}
 */
var makePrefSumNonNegative = function(nums) {
    const h = new Heap((a, b) => a - b);
    let sum = 0, ans = 0;
    for (const x of nums) {
        sum += x;
        if (x < 0) h.push(x);
        if (sum < 0) {
            const worst = h.pop();
            sum -= worst;
            ans++;
        }
    }
    return ans;
};
