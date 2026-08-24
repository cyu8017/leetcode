// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

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
MinHeap.prototype.peek = function() { return this.a[0]; };
MinHeap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums
 * @return {number}
 */
var convertArray = function(nums) {
    const cost = (arr) => {
        const h = new MinHeap((a, b) => b - a);
        let ans = 0;
        for (const x of arr) {
            if (h.size() && h.peek() > x) {
                const t = h.pop();
                ans += t - x;
                h.push(x);
            }
            h.push(x);
        }
        return ans;
    };
    const rev = nums.slice().reverse();
    return Math.min(cost(nums), cost(rev));
};
