// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

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
Heap.prototype.peek = function() { return this.a[0]; };
Heap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var maxScore = function(nums1, nums2, k) {
    const n = nums1.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => nums2[b] - nums2[a]);
    const pq = new Heap((a, b) => a - b);
    let sum = 0, ans = 0;
    for (const i of idx) {
        pq.push(nums1[i]);
        sum += nums1[i];
        if (pq.size() > k) sum -= pq.pop();
        if (pq.size() === k) {
            const cand = sum * nums2[i];
            if (cand > ans) ans = cand;
        }
    }
    return ans;
};
