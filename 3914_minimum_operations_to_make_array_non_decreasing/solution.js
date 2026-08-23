// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

var minOperations = function(nums) {
    let ans = 0;
    for (let i = 1; i < nums.length; i++) {
        ans += Math.max(0, nums[i - 1] - nums[i]);
    }
    return ans;
};
