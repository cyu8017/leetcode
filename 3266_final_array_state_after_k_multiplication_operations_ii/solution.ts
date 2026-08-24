// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

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

export function getFinalState(nums: any, k: any, multiplier: any): any {
    const mod = 1000000007;
    const modPow = (a, e, mod) => {
        let r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = Number((BigInt(r) * BigInt(a)) % BigInt(mod));
            a = Number((BigInt(a) * BigInt(a)) % BigInt(mod));
            e >>= 1;
        }
        return r;
    };
    if (multiplier === 1) return nums;
    const h = new MinHeap((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    let maxV = 0;
    for (let i = 0; i < nums.length; i++) {
        h.push([nums[i], i]);
        if (nums[i] > maxV) maxV = nums[i];
    }
    while (k > 0 && h.size()) {
        const cur = h.pop();
        const v = cur[0], i = cur[1];
        if (v * multiplier > maxV && k >= nums.length) {
            h.push([v, i]);
            break;
        }
        const nv = v * multiplier;
        nums[i] = nv;
        if (nv > maxV) maxV = nv;
        h.push([nv, i]);
        k--;
    }
    if (k > 0) {
        const n = nums.length;
        const full = Math.floor(k / n), rem = k % n;
        const powFull = modPow(multiplier, full, mod);
        for (let i = 0; i < n; i++) nums[i] = Number((BigInt(nums[i]) * BigInt(powFull)) % BigInt(mod));
        const hh = new MinHeap((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
        for (let i = 0; i < n; i++) hh.push([nums[i], i]);
        for (let t = 0; t < rem; t++) {
            const cur = hh.pop();
            const v = Number((BigInt(cur[0]) * BigInt(multiplier)) % BigInt(mod));
            const i = cur[1];
            nums[i] = v;
            hh.push([v, i]);
        }
        for (let i = 0; i < n; i++) nums[i] %= mod;
    } else {
        for (let i = 0; i < nums.length; i++) nums[i] %= mod;
    }
    return nums;
}
