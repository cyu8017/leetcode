// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    const value = (word) => {
        let s = "";
        for (const ch of word) s += String(ch.charCodeAt(0) - 97);
        return Number(s);
    };
    return value(firstWord) + value(secondWord) === value(targetWord);
};
