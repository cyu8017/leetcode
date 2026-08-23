// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

function UpperBound3911(a, x) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
var kthSmallestEven = function(nums, queries) {
    const n = nums.length;
    const evenPrefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 === 0 ? 1 : 0);
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const l = queries[qi][0], r = queries[qi][1];
        const k = queries[qi][2];
        let lo = 1, hi = k + (r - l + 1);
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            let pos = UpperBound3911(nums, 2 * mid);
            if (pos > r + 1) pos = r + 1;
            let removed = 0;
            if (pos > l) removed = evenPrefix[pos] - evenPrefix[l];
            if (mid - removed >= k) hi = mid;
            else lo = mid + 1;
        }
        ans[qi] = 2 * lo;
    }
    return ans;
};
