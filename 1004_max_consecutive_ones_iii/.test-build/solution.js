"use strict";
// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/
function longestOnes(nums, k) {
    let left = 0, zeros = 0, ans = 0;
    for (let right = 0; right < nums.length; right++) {
        zeros += nums[right] === 0 ? 1 : 0;
        while (zeros > k) {
            zeros -= nums[left] === 0 ? 1 : 0;
            left++;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
