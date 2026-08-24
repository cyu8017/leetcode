// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

export function handleQuery(nums1: number[], nums2: number[], queries: number[][]): number[] {
    const n = nums1.length;
    const ones = new Array(4 * n).fill(0);
    const lazy = new Array(4 * n).fill(false);
    const build = (idx, l, r) => {
        if (l === r) {
            ones[idx] = nums1[l];
            return;
        }
        const m = (l + r) >> 1;
        build(idx * 2, l, m);
        build(idx * 2 + 1, m + 1, r);
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
    };
    const apply = (idx, l, r) => {
        ones[idx] = (r - l + 1) - ones[idx];
        lazy[idx] = !lazy[idx];
    };
    const push = (idx, l, r) => {
        if (lazy[idx] && l !== r) {
            const m = (l + r) >> 1;
            apply(idx * 2, l, m);
            apply(idx * 2 + 1, m + 1, r);
            lazy[idx] = false;
        }
    };
    const update = (idx, l, r, ql, qr) => {
        if (ql <= l && r <= qr) {
            apply(idx, l, r);
            return;
        }
        push(idx, l, r);
        const m = (l + r) >> 1;
        if (ql <= m) update(idx * 2, l, m, ql, qr);
        if (qr > m) update(idx * 2 + 1, m + 1, r, ql, qr);
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
    };
    build(1, 0, n - 1);
    let sum2 = 0;
    for (const x of nums2) sum2 += x;
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) update(1, 0, n - 1, q[1], q[2]);
        else if (q[0] === 2) sum2 += q[1] * ones[1];
        else ans.push(sum2);
    }
    return ans;
}
