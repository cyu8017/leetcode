// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

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
 * @param {number[]} freq
 * @return {number[]}
 */
var mostFrequentIDs = function(nums, freq) {
    const n = nums.length;
    const cnt = new Map();
    const lazy = new Map();
    const ans = new Array(n);
    const pq = new MinHeap((a, b) => b - a);
    for (let i = 0; i < n; i++) {
        const x = nums[i], f = freq[i];
        const old = cnt.get(x) || 0;
        lazy.set(old, (lazy.get(old) || 0) + 1);
        const neu = old + f;
        cnt.set(x, neu);
        pq.push(neu);
        while (pq.size() && (lazy.get(pq.peek()) || 0) > 0) {
            const top = pq.pop();
            lazy.set(top, lazy.get(top) - 1);
        }
        if (pq.size()) ans[i] = pq.peek();
        else ans[i] = 0;
    }
    return ans;
};
