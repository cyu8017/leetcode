// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

function gcd3901(a, b) {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}
function SegmentTree3901(n) {
    this.tr = Array.from({length: n << 2}, () => ({l: 0, r: 0, g: 0}));
    this.build(1, 1, n);
}
SegmentTree3901.prototype.build = function(u, l, r) {
    this.tr[u].l = l; this.tr[u].r = r; this.tr[u].g = 0;
    if (l === r) return;
    const mid = (l + r) >> 1;
    this.build(u << 1, l, mid);
    this.build(u << 1 | 1, mid + 1, r);
};
SegmentTree3901.prototype.pushup = function(u) {
    this.tr[u].g = gcd3901(this.tr[u << 1].g, this.tr[u << 1 | 1].g);
};
SegmentTree3901.prototype.modify = function(u, x, v) {
    if (this.tr[u].l === this.tr[u].r) { this.tr[u].g = v; return; }
    const mid = (this.tr[u].l + this.tr[u].r) >> 1;
    if (x <= mid) this.modify(u << 1, x, v);
    else this.modify(u << 1 | 1, x, v);
    this.pushup(u);
};
SegmentTree3901.prototype.query = function(u, l, r) {
    if (l > r) return 0;
    if (this.tr[u].l >= l && this.tr[u].r <= r) return this.tr[u].g;
    const mid = (this.tr[u].l + this.tr[u].r) >> 1;
    if (r <= mid) return this.query(u << 1, l, r);
    if (l > mid) return this.query(u << 1 | 1, l, r);
    return gcd3901(this.query(u << 1, l, mid), this.query(u << 1 | 1, mid + 1, r));
};
var countGoodSubseq = function(nums, p, queries) {
    const n = nums.length;
    const tree = new SegmentTree3901(n);
    let cnt = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] % p === 0) {
            tree.modify(1, i + 1, nums[i]);
            cnt++;
        }
    }
    let ans = 0;
    for (const q of queries) {
        const idx = q[0], val = q[1];
        if (nums[idx] % p === 0) {
            tree.modify(1, idx + 1, 0);
            cnt--;
        }
        if (val % p === 0) {
            tree.modify(1, idx + 1, val);
            cnt++;
        }
        nums[idx] = val;
        if (tree.tr[1].g !== p) continue;
        if (cnt < n || n > 6) {
            ans++;
            continue;
        }
        for (let i = 1; i <= n; i++) {
            const leftG = tree.query(1, 1, i - 1);
            const rightG = tree.query(1, i + 1, n);
            if (gcd3901(leftG, rightG) === p) { ans++; break; }
        }
    }
    return ans;
};
