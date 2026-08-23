// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

/**
 * @param {string} s
 * @return {string}
 */
var finalString = function(s) {
    let b = '';
    for (const c of s) {
        if (c === 'i') b = b.split('').reverse().join('');
        else b += c;
    }
    return b;
};
