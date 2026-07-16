// LeetCode 0137 - Single Number II
// https://leetcode.com/problems/single-number-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ones = 0;
    let twos = 0;

    for (const num of nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }

    return ones;
};