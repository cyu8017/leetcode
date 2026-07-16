// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

/**
 * @param {number[]} nums
 * @return {void}
 */
var wiggleSort = function(nums) {
    for (let index = 1; index < nums.length; index++) {
        if (index % 2 === 1 && nums[index] < nums[index - 1]) {
            const tmp = nums[index];
            nums[index] = nums[index - 1];
            nums[index - 1] = tmp;
        } else if (index % 2 === 0 && nums[index] > nums[index - 1]) {
            const tmp = nums[index];
            nums[index] = nums[index - 1];
            nums[index - 1] = tmp;
        }
    }
};
