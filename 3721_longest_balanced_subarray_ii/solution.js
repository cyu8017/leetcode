// LeetCode 3721 - Longest Balanced Subarray Ii
// https://leetcode.com/problems/longest_balanced_subarray_ii/

var longestBalanced = function(nums) {
    class Node {
        constructor() { this.l = 0; this.r = 0; this.mn = 0; this.mx = 0; this.lazy = 0; }
    }
    class SegmentTree {
        constructor(n) {
            this.tr = Array.from({length: n << 2}, () => new Node());
            this.build(1, 0, n);
        }
        build(u, l, r) {
            const tr = this.tr;
            tr[u].l = l; tr[u].r = r; tr[u].mn = 0; tr[u].mx = 0; tr[u].lazy = 0;
            if (l === r) return;
            const mid = (l + r) >> 1;
            this.build(u << 1, l, mid);
            this.build(u << 1 | 1, mid + 1, r);
        }
        apply(u, v) {
            this.tr[u].mn += v;
            this.tr[u].mx += v;
            this.tr[u].lazy += v;
        }
        pushup(u) {
            const tr = this.tr;
            tr[u].mn = Math.min(tr[u << 1].mn, tr[u << 1 | 1].mn);
            tr[u].mx = Math.max(tr[u << 1].mx, tr[u << 1 | 1].mx);
        }
        pushdown(u) {
            if (this.tr[u].lazy !== 0) {
                const v = this.tr[u].lazy;
                this.apply(u << 1, v);
                this.apply(u << 1 | 1, v);
                this.tr[u].lazy = 0;
            }
        }
        modify(u, l, r, v) {
            const tr = this.tr;
            if (tr[u].l >= l && tr[u].r <= r) {
                this.apply(u, v);
                return;
            }
            this.pushdown(u);
            const mid = (tr[u].l + tr[u].r) >> 1;
            if (l <= mid) this.modify(u << 1, l, r, v);
            if (r > mid) this.modify(u << 1 | 1, l, r, v);
            this.pushup(u);
        }
        query(u, target) {
            const tr = this.tr;
            if (tr[u].l === tr[u].r) return tr[u].l;
            this.pushdown(u);
            const left = u << 1, right = u << 1 | 1;
            if (tr[left].mn <= target && target <= tr[left].mx) return this.query(left, target);
            return this.query(right, target);
        }
    }
    const n = nums.length;
    const st = new SegmentTree(n);
    const last = new Map();
    let now = 0, ans = 0;
    for (let i = 1; i <= n; i++) {
        const x = nums[i - 1];
        const det = (x & 1) !== 0 ? 1 : -1;
        if (last.has(x)) {
            st.modify(1, last.get(x), n, -det);
            now -= det;
        }
        last.set(x, i);
        st.modify(1, i, n, det);
        now += det;
        const pos = st.query(1, now);
        ans = Math.max(ans, i - pos);
    }
    return ans;
};
