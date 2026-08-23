// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumSubseqWidths = function(nums) {
    const MOD = 1000000007;
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pow2 = new Array(n);
    pow2[0] = 1;
    for (let i = 1; i < n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans = (ans + nums[i] * (pow2[i] - pow2[n - 1 - i])) % MOD;
    }
    return (ans + MOD) % MOD;
};
