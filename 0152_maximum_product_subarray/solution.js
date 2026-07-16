// LeetCode 0152 - Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

/**
 * Finds the largest product of a contiguous subarray.
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let best = nums[0];
    let maxProduct = nums[0];
    let minProduct = nums[0];

    for (let i = 1; i < nums.length; i += 1) {
        const num = nums[i];
        const previousMax = maxProduct;
        maxProduct = Math.max(num, previousMax * num, minProduct * num);
        minProduct = Math.min(num, previousMax * num, minProduct * num);
        best = Math.max(best, maxProduct);
    }

    return best;
};