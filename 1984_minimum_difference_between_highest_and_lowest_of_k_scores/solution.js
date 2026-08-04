// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    nums = nums.slice().sort((a, b) => a - b);
    let ans = Infinity;
    for (let i = 0; i + k - 1 < nums.length; i++) ans = Math.min(ans, nums[i + k - 1] - nums[i]);
    return ans;
};
