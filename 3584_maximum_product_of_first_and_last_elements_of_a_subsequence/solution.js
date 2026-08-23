// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

var maximumProduct = function(nums, m) {
    let ans = Number.MIN_SAFE_INTEGER;
    let mx = Number.MIN_SAFE_INTEGER, mi = Number.MAX_SAFE_INTEGER;
    for (let i = m - 1; i < nums.length; i++) {
        const x = nums[i], y = nums[i - m + 1];
        mi = Math.min(mi, y);
        mx = Math.max(mx, y);
        ans = Math.max(ans, Math.max(x * mi, x * mx));
    }
    return ans;
};
