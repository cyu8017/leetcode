// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

var maxTotalValue = function(nums, k) {
    let mn = nums[0], mx = nums[0];
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
    }
    return k * (mx - mn);
};
