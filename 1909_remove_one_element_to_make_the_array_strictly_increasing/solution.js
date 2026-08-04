// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    const check = (skip) => {
        let prev = null;
        for (let i = 0; i < nums.length; i++) {
            if (i === skip) continue;
            if (prev !== null && nums[i] <= prev) return false;
            prev = nums[i];
        }
        return true;
    };
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) return check(i - 1) || check(i);
    }
    return true;
};
