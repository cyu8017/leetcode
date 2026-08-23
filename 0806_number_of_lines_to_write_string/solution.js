// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function(widths, s) {
    let lines = 1, width = 0;
    for (const ch of s) {
        const w = widths[ch.charCodeAt(0) - 97];
        if (width + w > 100) {
            lines++;
            width = w;
        } else {
            width += w;
        }
    }
    return [lines, width];
};
