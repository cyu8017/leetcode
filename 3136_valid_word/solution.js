// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    if (word.length < 3) return false;
    let hasVowel = false, hasConsonant = false;
    const vs = new Array(26).fill(false);
    for (const c of "aeiou") vs[c.charCodeAt(0) - 97] = true;
    for (let i = 0; i < word.length; i++) {
        const c = word[i];
        if (/[a-zA-Z]/.test(c)) {
            const lower = c.toLowerCase();
            if (vs[lower.charCodeAt(0) - 97]) hasVowel = true;
            else hasConsonant = true;
        } else if (!/[0-9]/.test(c)) {
            return false;
        }
    }
    return hasVowel && hasConsonant;
};
