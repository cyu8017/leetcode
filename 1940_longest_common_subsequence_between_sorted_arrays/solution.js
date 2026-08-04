// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

/**
 * @param {number[][]} arrays
 * @return {number[]}
 */
var longestCommonSubsequence = function(arrays) {
    const cnt = new Map();
    for (const arr of arrays) {
        for (const x of arr) cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    const m = arrays.length;
    return arrays[0].filter((x) => cnt.get(x) === m);
};
