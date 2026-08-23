// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let first = -1, second = -1, index = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > first) { second = first; first = nums[i]; index = i; }
        else if (nums[i] > second) second = nums[i];
    }
    return first >= 2 * second ? index : -1;
};
