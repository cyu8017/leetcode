// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    const counts = new Map();
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const product = nums[i] * nums[j];
            counts.set(product, (counts.get(product) || 0) + 1);
        }
    }
    let result = 0;
    for (const count of counts.values()) {
        result += count * (count - 1) * 4;
    }
    return result;
};
