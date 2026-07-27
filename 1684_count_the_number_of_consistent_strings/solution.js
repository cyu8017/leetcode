// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    const a = new Set(allowed);
    return words.filter((w) => [...w].every((c) => a.has(c))).length;
};
