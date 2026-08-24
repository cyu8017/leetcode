// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const tree = Array.from({ length: 4 * (n + 2) }, () => ({ sum: 0, sumSq: 0, lazy: 0 }));
    const apply = (idx, l, r, val) => {
        const length = r - l + 1;
        tree[idx].sumSq = (tree[idx].sumSq + 2 * val % MOD * tree[idx].sum % MOD
            + val % MOD * val % MOD * length % MOD) % MOD;
        tree[idx].sum = (tree[idx].sum + val % MOD * length % MOD) % MOD;
        tree[idx].lazy = (tree[idx].lazy + val) % MOD;
    };
    const update = (idx, l, r, ql, qr, val) => {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(idx, l, r, val);
            return;
        }
        if (tree[idx].lazy !== 0 && l !== r) {
            const mid = Math.floor((l + r) / 2);
            apply(idx * 2, l, mid, tree[idx].lazy);
            apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy);
            tree[idx].lazy = 0;
        }
        const mid = Math.floor((l + r) / 2);
        update(idx * 2, l, mid, ql, qr, val);
        update(idx * 2 + 1, mid + 1, r, ql, qr, val);
        tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD;
        tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % MOD;
    };
    const last = new Map();
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        const v = nums[i - 1];
        const prev = last.get(v) || 0;
        update(1, 1, n, prev + 1, i, 1);
        ans = (ans + tree[1].sumSq) % MOD;
        last.set(v, i);
    }
    return ans;
};
