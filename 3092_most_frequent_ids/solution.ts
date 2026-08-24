// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

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

export function mostFrequentIDs(nums: number[], freq: number[]): number[] {
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
}
