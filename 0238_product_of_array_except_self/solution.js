// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const length = nums.length;
    const result = new Array(length).fill(1);
    let prefix = 1;
    for (let index = 0; index < length; index++) {
        result[index] = prefix;
        prefix *= nums[index];
    }
    let suffix = 1;
    for (let index = length - 1; index >= 0; index--) {
        result[index] *= suffix;
        suffix *= nums[index];
    }
    return result;
};
