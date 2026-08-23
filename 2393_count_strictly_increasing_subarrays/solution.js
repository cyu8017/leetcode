// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function(nums) {
    let ans = 0, len = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] > nums[i - 1]) len++;
        else len = 1;
        ans += len;
    }
    return ans;
};
