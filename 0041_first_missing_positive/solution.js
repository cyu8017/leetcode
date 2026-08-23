// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const n = nums.length;
    let i = 0;

    while (i < n) {
        const value = nums[i];
        const target = value - 1;
        if (value >= 1 && value <= n && nums[target] !== value) {
            [nums[i], nums[target]] = [nums[target], nums[i]];
        } else {
            i += 1;
        }
    }

    for (let index = 0; index < n; index += 1) {
        if (nums[index] !== index + 1) {
            return index + 1;
        }
    }

    return n + 1;
};
