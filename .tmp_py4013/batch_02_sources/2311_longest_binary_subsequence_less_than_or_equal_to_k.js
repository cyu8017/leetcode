// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubsequence = function(s, k) {
    let zeros = 0;
    for (let i = 0; i < s.length; i++) if (s[i] === '0') zeros++;
    let val = 0, ones = 0, pow = 1;
    for (let i = s.length - 1; i >= 0; --i) {
        if (s[i] === '1') {
            if (!(pow > k || val + pow > k)) {
                val += pow;
                ones++;
            }
        }
        if (pow <= k) {
            if (pow > Number.MAX_SAFE_INTEGER / 2) pow = k + 1;
            else pow *= 2;
        }
    }
    return zeros + ones;
};
