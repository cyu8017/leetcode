// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

class Fancy {
    constructor() {
        this.MOD = 1000000007;
        this.n = 0;
        this.size = 1 << 17;
        this.tree = Array(2 * this.size).fill(0);
        this.mul = Array(2 * this.size).fill(1);
        this.add = Array(2 * this.size).fill(0);
    }

    _apply(p, m, a) {
        this.tree[p] = (this.tree[p] * m + a) % this.MOD;
        this.mul[p] = (this.mul[p] * m) % this.MOD;
        this.add[p] = (this.add[p] * m + a) % this.MOD;
    }

    _push(p) {
        if (this.mul[p] !== 1 || this.add[p]) {
            this._apply(2 * p, this.mul[p], this.add[p]);
            this._apply(2 * p + 1, this.mul[p], this.add[p]);
            this.mul[p] = 1;
            this.add[p] = 0;
        }
    }

    _update(p, l, r, ql, qr, m, a) {
        if (ql <= l && r <= qr) {
            this._apply(p, m, a);
            return;
        }
        this._push(p);
        const mid = (l + r) >> 1;
        if (ql <= mid) this._update(2 * p, l, mid, ql, qr, m, a);
        if (qr > mid) this._update(2 * p + 1, mid + 1, r, ql, qr, m, a);
    }

    _get(p, l, r, i) {
        if (l === r) return this.tree[p];
        this._push(p);
        const mid = (l + r) >> 1;
        return i <= mid ? this._get(2 * p, l, mid, i) : this._get(2 * p + 1, mid + 1, r, i);
    }

    /**
     * @param {number} val
     * @return {null}
     */
    append(val) {
        this._update(1, 0, this.size - 1, this.n, this.n, 0, val % this.MOD);
        this.n++;
        return null;
    }

    /**
     * @param {number} inc
     * @return {null}
     */
    addAll(inc) {
        if (this.n) this._update(1, 0, this.size - 1, 0, this.n - 1, 1, inc % this.MOD);
        return null;
    }

    /**
     * @param {number} m
     * @return {null}
     */
    multAll(m) {
        if (this.n) this._update(1, 0, this.size - 1, 0, this.n - 1, m % this.MOD, 0);
        return null;
    }

    /**
     * @param {number} idx
     * @return {number}
     */
    getIndex(idx) {
        return idx < this.n ? this._get(1, 0, this.size - 1, idx) : -1;
    }
}

module.exports = { Fancy };
