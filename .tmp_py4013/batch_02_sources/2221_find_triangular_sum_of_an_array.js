// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var triangularSum = function(nums) {
    while (nums.length > 1) {
        const next = new Array(nums.length - 1);
        for (let i = 0; i < next.length; i++)
            next[i] = (nums[i] + nums[i + 1]) % 10;
        nums = next;
    }
    return nums[0];
};
