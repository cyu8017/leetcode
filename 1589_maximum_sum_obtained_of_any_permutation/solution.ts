// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
// @ts-nocheck

function maxSumRangeQuery(nums: number[], requests: number[][]): number {
    const MOD = 1000000007;
    const diff = Array(nums.length + 1).fill(0);
    for (const [left, right] of requests) {
        diff[left]++;
        diff[right + 1]--;
    }
    for (let i = 1; i < nums.length; i++) diff[i] += diff[i - 1];
    nums.sort((a, b) => a - b);
    const freq = diff.slice(0, nums.length).sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < nums.length; i++) ans = (ans + nums[i] * freq[i]) % MOD;
    return ans;
}
