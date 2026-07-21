// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {
    const counts = new Map();
    for (const word of words) {
        for (const ch of word) {
            counts.set(ch, (counts.get(ch) || 0) + 1);
        }
    }
    const n = words.length;
    for (const total of counts.values()) {
        if (total % n !== 0) return false;
    }
    return true;
};
