// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

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

export function convertArray(nums: number[]): number {
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
}
