// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    if (pattern.length !== words.length) {
        return false;
    }
    const charToWord = new Map();
    const wordToChar = new Map();
    for (let index = 0; index < pattern.length; index += 1) {
        const char = pattern[index];
        const word = words[index];
        if (charToWord.has(char)) {
            if (charToWord.get(char) !== word) {
                return false;
            }
        } else if (wordToChar.has(word)) {
            return false;
        } else {
            charToWord.set(char, word);
            wordToChar.set(word, char);
        }
    }
    return true;
};
