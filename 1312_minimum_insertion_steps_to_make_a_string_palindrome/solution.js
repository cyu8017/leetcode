// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    const n = s.length;
    const dp = Array(n).fill(0);
    for (let left = n - 2; left >= 0; left--) {
        let diagonal = 0;
        for (let right = left + 1; right < n; right++) {
            const old = dp[right];
            if (s[left] === s[right]) dp[right] = diagonal;
            else dp[right] = 1 + Math.min(dp[right], dp[right - 1]);
            diagonal = old;
        }
    }
    return dp.length ? dp[dp.length - 1] : 0;
};
