// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canDivideIntoSubsequences = function(nums, k) {
    const freq = new Map();
    let maxFreq = 0;
    for (const x of nums) {
        const f = (freq.get(x) || 0) + 1;
        freq.set(x, f);
        maxFreq = Math.max(maxFreq, f);
    }
    return nums.length >= k * maxFreq;
};
