// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    let best = 1, cur = 1;
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] > nums[i - 1]) {
            ++cur;
            best = Math.max(best, cur);
        } else {
            cur = 1;
        }
    }
    return best;
};
