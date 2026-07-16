// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

/**
 * @param {number[]} nums
 * @return {void}
 */
var moveZeroes = function(nums) {
    let insert = 0;
    for (const num of nums) {
        if (num !== 0) {
            nums[insert] = num;
            insert += 1;
        }
    }
    for (let index = insert; index < nums.length; index += 1) {
        nums[index] = 0;
    }
};
