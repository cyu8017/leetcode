// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle.length === 0) {
        return 0;
    }

    const needleLen = needle.length;
    for (let i = 0; i <= haystack.length - needleLen; i++) {
        if (haystack.slice(i, i + needleLen) === needle) {
            return i;
        }
    }

    return -1;
};
