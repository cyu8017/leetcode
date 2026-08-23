// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxArrayValue = function(nums) {
    const n = nums.length;
    let cur = nums[n - 1], ans = cur;
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= cur) cur += nums[i];
        else cur = nums[i];
        ans = Math.max(ans, cur);
    }
    return ans;
};
