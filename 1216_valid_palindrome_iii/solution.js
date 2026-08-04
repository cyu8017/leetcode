// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var isValidPalindrome = function(s, k) {
    const dp = Array(s.length).fill(0);
    for (let i = s.length - 1; i >= 0; i--) {
        let previous = 0;
        for (let j = i + 1; j < s.length; j++) {
            const old = dp[j];
            if (s[i] === s[j]) dp[j] = previous;
            else dp[j] = 1 + Math.min(dp[j], dp[j - 1]);
            previous = old;
        }
    }
    return !s.length || dp[s.length - 1] <= k;
};
