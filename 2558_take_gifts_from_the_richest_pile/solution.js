// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

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
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */
var pickGifts = function(gifts, k) {
    const h = new MaxHeap();
    for (const g of gifts) h.push(g);
    for (let i = 0; i < k; ++i) {
        const x = h.pop();
        h.push(Math.floor(Math.sqrt(x)));
    }
    let ans = 0;
    while (h.size()) ans += h.pop();
    return ans;
};
