// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

var maximumCount = function(nums, queries) {
    let mx = 0;
    for (const v of nums) mx = Math.max(mx, v);
    for (const q of queries) mx = Math.max(mx, q[1]);
    const isP = new Array(mx + 1).fill(false);
    for (let i = 2; i <= mx; i++) isP[i] = true;
    for (let i = 2; i * i <= mx; i++) {
        if (isP[i]) for (let j = i * i; j <= mx; j += i) isP[j] = false;
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        nums[queries[qi][0]] = queries[qi][1];
        let best = 0;
        const left = new Map(), right = new Map();
        for (const v of nums) if (v <= mx && isP[v]) right.set(v, (right.get(v) || 0) + 1);
        for (let i = 0; i < nums.length - 1; i++) {
            const v = nums[i];
            if (v <= mx && isP[v]) {
                left.set(v, (left.get(v) || 0) + 1);
                const c = right.get(v) - 1;
                if (c === 0) right.delete(v);
                else right.set(v, c);
            }
            best = Math.max(best, left.size + right.size);
        }
        ans[qi] = best;
    }
    return ans;
};
