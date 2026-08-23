// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    let pairs = 0, left = 0;
    for (const c of cnt.values()) {
        pairs += Math.floor(c / 2);
        left += c % 2;
    }
    return [pairs, left];
};
