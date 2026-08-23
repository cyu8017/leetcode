// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

var solveQueries = function(nums, queries) {
    const n = nums.length;
    const pos = new Map();
    for (let i = 0; i < n; i++) {
        if (!pos.has(nums[i])) pos.set(nums[i], []);
        pos.get(nums[i]).push(i);
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const idx = queries[qi];
        const x = nums[idx];
        const arr = pos.get(x);
        if (arr.length === 1) { ans[qi] = -1; continue; }
        let best = n;
        for (const p of arr) {
            if (p === idx) continue;
            let d = Math.abs(p - idx);
            d = Math.min(d, n - d);
            if (d < best) best = d;
        }
        ans[qi] = best;
    }
    return ans;
};
