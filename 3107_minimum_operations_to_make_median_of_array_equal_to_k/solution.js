// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperationsToMakeMedianK = function(nums, k) {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length, m = n >> 1;
    let ans = Math.abs(nums[m] - k);
    if (nums[m] > k) {
        for (let i = m - 1; i >= 0 && nums[i] > k; i--) ans += nums[i] - k;
    } else {
        for (let i = m + 1; i < n && nums[i] < k; i++) ans += k - nums[i];
    }
    return ans;
};
