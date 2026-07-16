// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let length = 0;
    let i = s.length - 1;

    while (i >= 0 && s[i] === ' ') {
        i -= 1;
    }

    while (i >= 0 && s[i] !== ' ') {
        length += 1;
        i -= 1;
    }

    return length;
};
