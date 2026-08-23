// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

function ok(up, n, k) {
    for (let i = 0; i + 2 * k <= n; i++) {
        if (up[i] >= k && up[i + k] >= k) return true;
    }
    return false;
}
var maxIncreasingSubarrays = function(nums) {
    const n = nums.length;
    const up = new Array(n);
    up[n - 1] = 1;
    for (let i = n - 2; i >= 0; i--) {
        up[i] = (nums[i] < nums[i + 1]) ? up[i + 1] + 1 : 1;
    }
    let lo = 1, hi = Math.floor(n / 2);
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(up, n, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
