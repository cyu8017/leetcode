// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countSpecialSubsequences = function(nums) {
    const MOD = 1000000007;
    let a = 0, b = 0, c = 0;
    for (const x of nums) {
        if (x === 0) a = (a * 2 + 1) % MOD;
        else if (x === 1) b = (b * 2 + a) % MOD;
        else c = (c * 2 + b) % MOD;
    }
    return c;
};
