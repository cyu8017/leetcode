// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

export function lengthOfLIS(nums: number[], k: number): number {
    let maxV = 0;
    for (const x of nums) maxV = Math.max(maxV, x);
    const tree = Array(4 * (maxV + 1)).fill(0);
    const update = (idx, l, r, pos, val) => {
        if (l === r) {
            tree[idx] = Math.max(tree[idx], val);
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx * 2, l, mid, pos, val);
        else update(idx * 2 + 1, mid + 1, r, pos, val);
        tree[idx] = Math.max(tree[idx * 2], tree[idx * 2 + 1]);
    };
    const query = (idx, l, r, ql, qr) => {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[idx];
        const mid = (l + r) >> 1;
        return Math.max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr));
    };
    let ans = 0;
    for (const x of nums) {
        const lo = Math.max(1, x - k);
        let best = 1;
        if (lo <= x - 1) best = query(1, 1, maxV, lo, x - 1) + 1;
        update(1, 1, maxV, x, best);
        ans = Math.max(ans, best);
    }
    return ans;
}
