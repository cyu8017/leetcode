// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var lengthOfLongestSubsequence = function(nums, target) {
    const dp = Array(target + 1).fill(-1);
    dp[0] = 0;
    for (const v of nums)
        for (let s = target; s >= v; s--)
            if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
    return dp[target];
};
