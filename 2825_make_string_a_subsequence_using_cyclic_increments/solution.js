// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

/**
 * @param {string} str1
 * @param {string} str2
 * @return {boolean}
 */
var canMakeSubsequence = function(str1, str2) {
    let j = 0;
    for (let i = 0; i < str1.length && j < str2.length; i++) {
        const a = str1.charCodeAt(i) - 97;
        const b = str2.charCodeAt(j) - 97;
        if (a === b || (a + 1) % 26 === b) j++;
    }
    return j === str2.length;
};
