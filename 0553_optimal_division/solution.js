// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

/**
 * @param {number[]} nums
 * @return {string}
 */
var optimalDivision = function(nums) {
    if (nums.length === 1) return String(nums[0]);
    if (nums.length === 2) return nums[0] + "/" + nums[1];
    let result = nums[0] + "/(";
    for (let i = 1; i < nums.length; ++i) {
        if (i > 1) result += "/";
        result += nums[i];
    }
    result += ")";
    return result;
};
