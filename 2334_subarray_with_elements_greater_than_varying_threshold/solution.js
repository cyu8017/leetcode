// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var validSubarraySize = function(nums, threshold) {
    const n = nums.length;
    const left = Array(n), right = Array(n);
    const stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        left[i] = stack.length === 0 ? -1 : stack[stack.length - 1];
        stack.push(i);
    }
    stack.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length > 0 && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        right[i] = stack.length === 0 ? n : stack[stack.length - 1];
        stack.push(i);
    }
    for (let i = 0; i < n; i++) {
        const k = right[i] - left[i] - 1;
        if (nums[i] > Math.floor(threshold / k)) return k;
    }
    return -1;
};
