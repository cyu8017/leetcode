// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    const seen = new Set();
    for (const x of nums) {
        if (seen.has(x)) return x;
        seen.add(x);
    }
    return -1;
};
