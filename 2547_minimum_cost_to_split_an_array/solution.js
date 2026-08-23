// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCost = function(nums, k) {
    const n = nums.length;
    const INF = Number.MAX_SAFE_INTEGER / 2;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < n; ++i) {
        const freq = new Map();
        let trimmed = 0;
        for (let j = i; j < n; ++j) {
            const c = (freq.get(nums[j]) || 0) + 1;
            freq.set(nums[j], c);
            if (c === 2) trimmed += 2;
            else if (c > 2) trimmed++;
            const cost = dp[i] + k + trimmed;
            if (cost < dp[j + 1]) dp[j + 1] = cost;
        }
    }
    return dp[n];
};
