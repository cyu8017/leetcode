"use strict";
// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/
function maximumScore(nums, k) {
    const n = nums.length;
    const stack = [];
    let ans = 0;
    for (let i = 0; i <= n; i++) {
        while (stack.length > 0 && (i === n || nums[i] < nums[stack[stack.length - 1]])) {
            const mid = stack.pop();
            const left = stack.length > 0 ? stack[stack.length - 1] + 1 : 0;
            const right = i - 1;
            if (left <= k && k <= right) {
                ans = Math.max(ans, nums[mid] * (right - left + 1));
            }
        }
        stack.push(i);
    }
    return ans;
}
