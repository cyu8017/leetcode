// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

export class MinHeap {
    constructor(cmp: any) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
    _up(i: any): any {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
}
    _down(i: any): any {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
}
    push(x: any): any { this.a.push(x); this._up(this.a.length - 1); }
    pop(): any {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
}
    peek(): any { return this.a[0]; }
    size(): any { return this.a.length; }
}

export function totalCost(costs: number[], k: number, candidates: number): number {
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
}
