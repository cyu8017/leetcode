// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

export class Fancy {
    private readonly MOD = 1000000007;
    private n = 0;
    private readonly size = 1 << 17;
    private readonly tree: number[];
    private readonly mul: number[];
    private readonly add: number[];

    constructor() {
        this.tree = Array(2 * this.size).fill(0);
        this.mul = Array(2 * this.size).fill(1);
        this.add = Array(2 * this.size).fill(0);
    }

    private apply(p: number, m: number, a: number): void {
        this.tree[p] = (this.tree[p] * m + a) % this.MOD;
        this.mul[p] = (this.mul[p] * m) % this.MOD;
        this.add[p] = (this.add[p] * m + a) % this.MOD;
    }

    private push(p: number): void {
        if (this.mul[p] !== 1 || this.add[p]) {
            this.apply(2 * p, this.mul[p], this.add[p]);
            this.apply(2 * p + 1, this.mul[p], this.add[p]);
            this.mul[p] = 1;
            this.add[p] = 0;
        }
    }

    private update(p: number, l: number, r: number, ql: number, qr: number, m: number, a: number): void {
        if (ql <= l && r <= qr) {
            this.apply(p, m, a);
            return;
        }
        this.push(p);
        const mid = (l + r) >> 1;
        if (ql <= mid) this.update(2 * p, l, mid, ql, qr, m, a);
        if (qr > mid) this.update(2 * p + 1, mid + 1, r, ql, qr, m, a);
    }

    private get(p: number, l: number, r: number, i: number): number {
        if (l === r) return this.tree[p];
        this.push(p);
        const mid = (l + r) >> 1;
        return i <= mid ? this.get(2 * p, l, mid, i) : this.get(2 * p + 1, mid + 1, r, i);
    }

    append(val: number): null {
        this.update(1, 0, this.size - 1, this.n, this.n, 0, val % this.MOD);
        this.n++;
        return null;
    }

    addAll(inc: number): null {
        if (this.n) this.update(1, 0, this.size - 1, 0, this.n - 1, 1, inc % this.MOD);
        return null;
    }

    multAll(m: number): null {
        if (this.n) this.update(1, 0, this.size - 1, 0, this.n - 1, m % this.MOD, 0);
        return null;
    }

    getIndex(idx: number): number {
        return idx < this.n ? this.get(1, 0, this.size - 1, idx) : -1;
    }
}
