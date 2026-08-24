// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

/**
 * @param {number} n
 * @param {number} m
 */
var BookMyShow = function(n, m) {
    this.n = n;
    this.m = m;
    this.sum = new Array(4 * n).fill(0);
    this.mx = new Array(4 * n).fill(0);
    const self = this;
    const pull = (idx) => {
        self.sum[idx] = self.sum[idx * 2] + self.sum[idx * 2 + 1];
        self.mx[idx] = Math.max(self.mx[idx * 2], self.mx[idx * 2 + 1]);
    };
    const build = (idx, l, r) => {
        if (l === r) {
            self.sum[idx] = self.mx[idx] = m;
            return;
        }
        const mid = (l + r) >> 1;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        pull(idx);
    };
    this._pull = pull;
    this._build = build;
    this._update = function(idx, l, r, pos, val) {
        if (l === r) {
            self.sum[idx] = self.mx[idx] = val;
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) self._update(idx * 2, l, mid, pos, val);
        else self._update(idx * 2 + 1, mid + 1, r, pos, val);
        pull(idx);
    };
    this._querySum = function(idx, l, r, ql, qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return self.sum[idx];
        const mid = (l + r) >> 1;
        return self._querySum(idx * 2, l, mid, ql, qr) + self._querySum(idx * 2 + 1, mid + 1, r, ql, qr);
    };
    this._findFirst = function(idx, l, r, maxRow, k) {
        if (l > maxRow || self.mx[idx] < k) return -1;
        if (l === r) return l;
        const mid = (l + r) >> 1;
        const left = self._findFirst(idx * 2, l, mid, maxRow, k);
        if (left !== -1) return left;
        return self._findFirst(idx * 2 + 1, mid + 1, r, maxRow, k);
    };
    build(1, 0, n - 1);
};

BookMyShow.prototype.gather = function(k, maxRow) {
    const row = this._findFirst(1, 0, this.n - 1, maxRow, k);
    if (row === -1) return [];
    const remain = this._querySum(1, 0, this.n - 1, row, row);
    const seat = this.m - remain;
    this._update(1, 0, this.n - 1, row, remain - k);
    return [row, seat];
};

BookMyShow.prototype.scatter = function(k, maxRow) {
    if (this._querySum(1, 0, this.n - 1, 0, maxRow) < k) return false;
    let need = k;
    for (let row = 0; row <= maxRow && need > 0; row++) {
        const remain = this._querySum(1, 0, this.n - 1, row, row);
        if (remain === 0) continue;
        const take = Math.min(remain, need);
        this._update(1, 0, this.n - 1, row, remain - take);
        need -= take;
    }
    return true;
};
