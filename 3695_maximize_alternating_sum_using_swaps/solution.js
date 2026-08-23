// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

var maxAlternatingSum = function(nums, swaps) {
    const n = nums.length;
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    for (const s of swaps) {
        const a = find(s[0]), b = find(s[1]);
        if (a !== b) parent[a] = b;
    }
    const compVals = new Map();
    const compIdx = new Map();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        if (!compVals.has(r)) { compVals.set(r, []); compIdx.set(r, []); }
        compVals.get(r).push(nums[i]);
        compIdx.get(r).push(i);
    }
    const arr = new Array(n);
    for (const [r, vals] of compVals) {
        const idxs = compIdx.get(r);
        vals.sort((a, b) => b - a);
        const even = [], odd = [];
        for (const i of idxs) {
            if (i % 2 === 0) even.push(i);
            else odd.push(i);
        }
        even.sort((a, b) => a - b);
        odd.sort((a, b) => a - b);
        let ei = 0;
        for (const v of vals) {
            if (ei < even.length) {
                arr[even[ei]] = v;
                ei++;
            } else {
                arr[odd[ei - even.length]] = v;
                ei++;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (i % 2 === 0) ans += arr[i];
        else ans -= arr[i];
    }
    return ans;
};
