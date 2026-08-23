// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubarraySplits = function(nums) {
    const MOD = 1000000007;
    const ones = [];
    for (let i = 0; i < nums.length; i++) if (nums[i] === 1) ones.push(i);
    if (!ones.length) return 0;
    let ans = 1;
    for (let i = 1; i < ones.length; i++)
        ans = ans * (ones[i] - ones[i - 1]) % MOD;
    return ans;
};
