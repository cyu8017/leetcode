// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

/**
 * @param {string} s
 * @return {string}
 */
var removeVowels = function(s) {
    return s.replace(/[aeiou]/g, "");
};
