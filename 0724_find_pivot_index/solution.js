// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let total = 0;
    for (const x of nums) total += x;
    let left = 0;
    for (let i = 0; i < nums.length; i++) {
        if (left === total - left - nums[i]) return i;
        left += nums[i];
    }
    return -1;
};
