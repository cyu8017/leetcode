// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

/**
 * @param {string} s
 * @return {boolean}
 */
var makePalindrome = function(s) {
    let diff = 0;
    for (let i = 0, j = s.length - 1; i < j; ++i, --j) {
        if (s[i] !== s[j]) {
            diff++;
            if (diff > 2) return false;
        }
    }
    return true;
};
