// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minImpossibleOR = function(nums) {
    const set = new Set(nums);
    let x = 1;
    while (set.has(x)) x <<= 1;
    return x;
};
