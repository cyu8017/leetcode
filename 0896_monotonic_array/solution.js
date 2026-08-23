// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    let inc = true, dec = true;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) inc = false;
        if (nums[i] > nums[i - 1]) dec = false;
    }
    return inc || dec;
};
