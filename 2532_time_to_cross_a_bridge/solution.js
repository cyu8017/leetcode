// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

function Heap(cmp) {
    this.a = [];
    this.cmp = cmp;
}
Heap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
Heap.prototype._down = function(i) {
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
Heap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
Heap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
Heap.prototype.peek = function() { return this.a[0]; };
Heap.prototype.size = function() { return this.a.length; };

/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} time
 * @return {number}
 */
var findCrossingTime = function(n, k, time) {
    const cmpW = (a, b) => {
        if (a.efficiency !== b.efficiency) return b.efficiency - a.efficiency;
        return b.idx - a.idx;
    };
    const left = new Heap(cmpW);
    const right = new Heap(cmpW);
    const ws = new Array(k);
    for (let i = 0; i < k; i++) {
        const t = time[i];
        ws[i] = {
            idx: i,
            leftToRight: t[0],
            pickOld: t[1],
            rightToLeft: t[2],
            putNew: t[3],
            efficiency: t[0] + t[2],
        };
        left.push(ws[i]);
    }
    const events = new Heap((a, b) => a[0] - b[0]);
    let cur = 0, bridgeFree = 0, remain = n, done = 0;
    while (done < n) {
        while (events.size() && events.peek()[0] <= cur) {
            const e = events.pop();
            const w = ws[e[2]];
            if (e[1] === 0) left.push(w);
            else right.push(w);
        }
        if (cur < bridgeFree) {
            cur = bridgeFree;
            continue;
        }
        if (right.size()) {
            const w = right.pop();
            cur += w.rightToLeft;
            bridgeFree = cur;
            events.push([cur + w.putNew, 0, w.idx]);
            done++;
            continue;
        }
        if (left.size() && remain > 0) {
            const w = left.pop();
            cur += w.leftToRight;
            bridgeFree = cur;
            remain--;
            events.push([cur + w.pickOld, 1, w.idx]);
            continue;
        }
        if (!events.size()) break;
        cur = events.peek()[0];
    }
    return cur;
};
