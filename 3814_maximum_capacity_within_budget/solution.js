// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum_capacity_within_budget/

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
var maxCapacity = function(costs, capacity, budget) {
    const arr = [];
    for (let k = 0; k < costs.length; k++) {
        if (costs[k] < budget) arr.push([costs[k], capacity[k]]);
    }
    if (!arr.length) return 0;
    arr.sort((a, b) => a[0] - b[0]);
    const m = arr.length;
    const alive = new Array(m).fill(true);
    const h = new MinHeap((a, b) => {
        if (a[0] !== b[0]) return b[0] - a[0];
        return b[1] - a[1];
    });
    for (let i = 0; i < m; i++) h.push([arr[i][1], i]);
    while (h.size() && !alive[h.peek()[1]]) h.pop();
    let ans = h.peek()[0];
    let i = 0, j = m - 1;
    while (i < j) {
        alive[i] = false;
        while (i < j && arr[i][0] + arr[j][0] >= budget) {
            alive[j] = false;
            j--;
        }
        while (h.size() && !alive[h.peek()[1]]) h.pop();
        if (h.size()) ans = Math.max(ans, arr[i][1] + h.peek()[0]);
        i++;
    }
    return ans;
};
