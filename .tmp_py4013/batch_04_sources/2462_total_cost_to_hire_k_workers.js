// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

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
 * @param {number[]} costs
 * @param {number} k
 * @param {number} candidates
 * @return {number}
 */
var totalCost = function(costs, k, candidates) {
    const cmp = (a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1];
    const leftH = new MinHeap(cmp), rightH = new MinHeap(cmp);
    const n = costs.length;
    let l = 0, r = n - 1;
    while (l <= r && leftH.size() < candidates) {
        leftH.push([costs[l], l]);
        l++;
    }
    while (r >= l && rightH.size() < candidates) {
        rightH.push([costs[r], r]);
        r--;
    }
    let ans = 0;
    for (let t = 0; t < k; t++) {
        let useLeft = false;
        if (leftH.size() && rightH.size()) {
            const lt = leftH.peek(), rt = rightH.peek();
            if (lt[0] < rt[0] || (lt[0] === rt[0] && lt[1] <= rt[1])) useLeft = true;
        } else if (leftH.size()) {
            useLeft = true;
        }
        if (useLeft) {
            ans += leftH.pop()[0];
            if (l <= r) {
                leftH.push([costs[l], l]);
                l++;
            }
        } else {
            ans += rightH.pop()[0];
            if (l <= r) {
                rightH.push([costs[r], r]);
                r--;
            }
        }
    }
    return ans;
};
