// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

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

export function minimizeStringValue(s: string): string {
    const cnt = new Array(26).fill(0);
    let k = 0;
    for (const c of s) {
        if (c === '?') k++;
        else cnt[c.charCodeAt(0) - 97]++;
    }
    const pq = new MinHeap((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    for (let i = 0; i < 26; i++) pq.push([cnt[i], i]);
    const t = new Array(k);
    for (let i = 0; i < k; i++) {
        const p = pq.pop();
        t[i] = p[1];
        p[0]++;
        pq.push(p);
    }
    t.sort((a, b) => a - b);
    const arr = s.split('');
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === '?') {
            arr[i] = String.fromCharCode(t[j] + 97);
            j++;
        }
    }
    return arr.join('');
}
