// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function maximumSumSubsequence(nums: number[], queries: number[][]): number {
    const n = nums.length;
    function Node(): any {
        this.l = 0; this.r = 0;
        this.s00 = 0; this.s01 = 0; this.s10 = 0; this.s11 = 0;
    }    const tr = Array.from({ length: n * 4 }, () => new Node());
    const build = (u, l, r) => {
        tr[u].l = l; tr[u].r = r;
        if (l === r) return;
        const mid = (l + r) >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
    };
    const pushup = (u) => {
        const left = tr[u << 1], right = tr[u << 1 | 1];
        tr[u].s00 = Math.max(left.s00 + right.s10, left.s01 + right.s00);
        tr[u].s01 = Math.max(left.s00 + right.s11, left.s01 + right.s01);
        tr[u].s10 = Math.max(left.s10 + right.s10, left.s11 + right.s00);
        tr[u].s11 = Math.max(left.s10 + right.s11, left.s11 + right.s01);
    };
    const modify = (u, x, v) => {
        if (tr[u].l === tr[u].r) {
            tr[u].s11 = Math.max(0, v);
            return;
        }
        const mid = (tr[u].l + tr[u].r) >> 1;
        if (x <= mid) modify(u << 1, x, v);
        else modify(u << 1 | 1, x, v);
        pushup(u);
    };
    const query = (u, l, r) => {
        if (tr[u].l >= l && tr[u].r <= r) return tr[u].s11;
        const mid = (tr[u].l + tr[u].r) >> 1;
        let ans = 0;
        if (r <= mid) ans = query(u << 1, l, r);
        if (l > mid) ans = Math.max(ans, query(u << 1 | 1, l, r));
        return ans;
    };
    build(1, 1, n);
    for (let i = 0; i < n; i++) modify(1, i + 1, nums[i]);
    const MOD = 1000000007;
    let ans = 0;
    for (const q of queries) {
        modify(1, q[0] + 1, q[1]);
        ans = (ans + query(1, 1, n)) % MOD;
    }
    return ans;
}
