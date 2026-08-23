// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxWidthRamp = function(nums) {
    const stack = [];
    for (let i = 0; i < nums.length; i++) {
        if (!stack.length || nums[stack[stack.length - 1]] > nums[i]) stack.push(i);
    }
    let ans = 0;
    for (let j = nums.length - 1; j >= 0; j--) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[j]) {
            ans = Math.max(ans, j - stack[stack.length - 1]);
            stack.pop();
        }
    }
    return ans;
};
