// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestArithSeqLength = function(nums) {
    const dp = Array.from({ length: nums.length }, () => new Map());
    let ans = 1;
    for (let j = 1; j < nums.length; j++) {
        for (let i = 0; i < j; i++) {
            const d = nums[j] - nums[i];
            const len = (dp[i].get(d) || 1) + 1;
            dp[j].set(d, len);
            ans = Math.max(ans, len);
        }
    }
    return ans;
};
