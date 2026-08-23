// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

/**
 * @param {string} s
 * @return {boolean}
 */
var canPermutePalindrome = function(s) {
    const counts = new Array(26).fill(0);
    for (const char of s) {
        counts[char.charCodeAt(0) - 97]++;
    }
    let odd = 0;
    for (const count of counts) {
        if (count % 2) {
            odd++;
        }
    }
    return odd <= 1;
};
