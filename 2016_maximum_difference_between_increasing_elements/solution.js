// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let ans = -1, mn = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > mn) ans = Math.max(ans, nums[i] - mn);
        else mn = nums[i];
    }
    return ans;
};
