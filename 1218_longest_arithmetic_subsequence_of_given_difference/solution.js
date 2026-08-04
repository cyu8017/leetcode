// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    const dp = new Map();
    let best = 0;
    for (const x of arr) {
        const v = (dp.get(x - difference) || 0) + 1;
        dp.set(x, v);
        best = Math.max(best, v);
    }
    return best;
};
