// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

function lowerBound(a, x) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}
function upperBound(a, x) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] <= x) lo = mid + 1; else hi = mid;
    }
    return lo;
}
var maxFrequency = function(nums, k, numOperations) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    let ans = 1;
    for (const [t, f] of freq) {
        const lo = lowerBound(nums, t - k);
        const hi = upperBound(nums, t + k);
        const can = hi - lo;
        const use = Math.min(can, f + numOperations);
        if (use > ans) ans = use;
    }
    let l = 0;
    for (let r = 0; r < n; r++) {
        while (nums[r] - nums[l] > 2 * k) l++;
        const window = Math.min(r - l + 1, numOperations);
        if (window > ans) ans = window;
    }
    return ans;
};
