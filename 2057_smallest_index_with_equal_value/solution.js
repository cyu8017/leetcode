// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestEqual = function(nums) {
    for (let i = 0; i < nums.length; i++)
        if (i % 10 === nums[i]) return i;
    return -1;
};
