// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const codes = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ];
    const seen = new Set();
    for (const word of words) {
        let code = "";
        for (const ch of word) code += codes[ch.charCodeAt(0) - 97];
        seen.add(code);
    }
    return seen.size;
};
