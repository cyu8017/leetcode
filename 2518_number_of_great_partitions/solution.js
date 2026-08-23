// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPartitions = function(nums, k) {
    const MOD = 1000000007;
    let sum = 0;
    for (const x of nums) sum += x;
    if (sum < 2 * k) return 0;
    const dp = Array(k).fill(0);
    dp[0] = 1;
    for (const x of nums) {
        for (let s = k - 1; s >= x; s--)
            dp[s] = (dp[s] + dp[s - x]) % MOD;
    }
    let bad = 0;
    for (const v of dp) bad = (bad + v) % MOD;
    let total = 1;
    for (let i = 0; i < nums.length; i++) total = total * 2 % MOD;
    return (total - 2 * bad % MOD + MOD) % MOD;
};
