// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

/**
 * @param {string} word
 * @return {string[]}
 */
var generateAbbreviations = function(word) {
    const result = [];
    function backtrack(index, path, count) {
        if (index === word.length) {
            result.push(path + (count ? String(count) : ""));
            return;
        }
        backtrack(index + 1, path, count + 1);
        backtrack(index + 1, path + (count ? String(count) : "") + word[index], 0);
    }
    backtrack(0, "", 0);
    return result;
};
