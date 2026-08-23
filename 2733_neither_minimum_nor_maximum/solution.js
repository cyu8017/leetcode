// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    if (nums.length < 3) return -1;
    const a = nums[0], b = nums[1], c = nums[2];
    return a + b + c - Math.max(a, b, c) - Math.min(a, b, c);
};
