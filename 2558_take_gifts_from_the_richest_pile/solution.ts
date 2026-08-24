// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

export class MaxHeap {
    constructor() {
    this.a = [];
}
    _up(i: any): any {
    const a = this.a;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (a[i] <= a[p]) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
}
    _down(i: any): any {
    const a = this.a, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && a[l] > a[s]) s = l;
        if (r < n && a[r] > a[s]) s = r;
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
    size(): any { return this.a.length; }
}

export function pickGifts(gifts: number[], k: number): number {
    const h = new MaxHeap();
    for (const g of gifts) h.push(g);
    for (let i = 0; i < k; ++i) {
        const x = h.pop();
        h.push(Math.floor(Math.sqrt(x)));
    }
    let ans = 0;
    while (h.size()) ans += h.pop();
    return ans;
}
