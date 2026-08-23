// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

/**
 * @param {string} order
 * @param {string} s
 * @return {string}
 */
var customSortString = function(order, s) {
    const count = new Array(26).fill(0);
    for (const ch of s) count[ch.charCodeAt(0) - 97]++;
    let sb = "";
    for (const ch of order) {
        const idx = ch.charCodeAt(0) - 97;
        while (count[idx]-- > 0) sb += ch;
    }
    for (let i = 0; i < 26; i++) {
        while (count[i]-- > 0) sb += String.fromCharCode(97 + i);
    }
    return sb;
};
