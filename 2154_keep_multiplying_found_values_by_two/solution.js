// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    const have = new Set(nums);
    while (have.has(original)) original *= 2;
    return original;
};
