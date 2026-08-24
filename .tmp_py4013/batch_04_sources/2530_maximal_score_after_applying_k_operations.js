// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

function MaxHeap() {
    this.a = [];
}
MaxHeap.prototype._up = function(i) {
    const a = this.a;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (a[i] <= a[p]) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MaxHeap.prototype._down = function(i) {
    const a = this.a, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && a[l] > a[s]) s = l;
        if (r < n && a[r] > a[s]) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MaxHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MaxHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MaxHeap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxKelements = function(nums, k) {
    const pq = new MaxHeap();
    for (const x of nums) pq.push(x);
    let ans = 0;
    for (let i = 0; i < k; i++) {
        const x = pq.pop();
        ans += x;
        pq.push(Math.floor((x + 2) / 3));
    }
    return ans;
};
