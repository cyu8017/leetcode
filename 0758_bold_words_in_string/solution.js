// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

/**
 * @param {string[]} words
 * @param {string} s
 * @return {string}
 */
var boldWords = function(words, s) {
    const n = s.length;
    const bold = new Array(n).fill(false);
    for (const word of words) {
        let start = s.indexOf(word);
        while (start >= 0) {
            for (let i = start; i < start + word.length; i++) bold[i] = true;
            start = s.indexOf(word, start + 1);
        }
    }
    let parts = '';
    let i2 = 0;
    while (i2 < n) {
        if (bold[i2]) {
            parts += '**';
            while (i2 < n && bold[i2]) parts += s[i2++];
            parts += '**';
        } else parts += s[i2++];
    }
    return parts;
};
