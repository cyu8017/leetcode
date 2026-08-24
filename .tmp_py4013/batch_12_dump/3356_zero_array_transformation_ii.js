// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

function ok(k, nums, queries, n) {
    const diff = new Array(n + 1).fill(0);
    for (let i = 0; i < k; i++) {
        const q = queries[i];
        diff[q[0]] += q[2];
        diff[q[1] + 1] -= q[2];
    }
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        if (cur < nums[i]) return false;
    }
    return true;
}
var minZeroArray = function(nums, queries) {
    const n = nums.length;
    if (ok(0, nums, queries, n)) return 0;
    let lo = 1, hi = queries.length + 1;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (mid <= queries.length && ok(mid, nums, queries, n)) hi = mid;
        else lo = mid + 1;
    }
    if (lo > queries.length) return -1;
    return lo;
};
