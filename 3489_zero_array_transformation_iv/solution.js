// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

var minZeroArray = function(nums, queries) {
    const canSubsetSum = (vals, target) => {
        if (target === 0) return true;
        const dp = new Array(target + 1).fill(false);
        dp[0] = true;
        for (const v of vals) {
            for (let s = target; s >= v; s--) if (dp[s - v]) dp[s] = true;
        }
        return dp[target];
    };
    const ok = (k) => {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 0) continue;
            const vals = [];
            for (let q = 0; q < k; q++) {
                const l = queries[q][0], r = queries[q][1], v = queries[q][2];
                if (l <= i && i <= r) vals.push(v);
            }
            if (!canSubsetSum(vals, nums[i])) return false;
        }
        return true;
    };
    if (ok(0)) return 0;
    let lo = 1, hi = queries.length + 1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (mid <= queries.length && ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo > queries.length ? -1 : lo;
};
