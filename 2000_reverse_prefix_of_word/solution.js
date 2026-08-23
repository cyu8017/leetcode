// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    const pos = word.indexOf(ch);
    if (pos < 0) return word;
    const arr = word.split('');
    for (let l = 0, r = pos; l < r; l++, r--) {
        const tmp = arr[l];
        arr[l] = arr[r];
        arr[r] = tmp;
    }
    return arr.join('');
};
