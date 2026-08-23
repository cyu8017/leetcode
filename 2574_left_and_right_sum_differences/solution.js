// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {
    let total = 0;
    for (const x of nums) total += x;
    const ans = new Array(nums.length);
    let left = 0;
    for (let i = 0; i < nums.length; ++i) {
        const right = total - left - nums[i];
        ans[i] = Math.abs(left - right);
        left += nums[i];
    }
    return ans;
};
