// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    const sorted = [...nums].sort((a, b) => a - b);
    return nums.map((x) => sorted.indexOf(x));
};
