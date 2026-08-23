// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximizeGreatness = function(nums) {
    nums.sort((a, b) => a - b);
    let i = 0;
    for (const x of nums) {
        if (x > nums[i]) i++;
    }
    return i;
};
