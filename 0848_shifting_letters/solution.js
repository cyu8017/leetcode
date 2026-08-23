// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

/**
 * @param {string} s
 * @param {number[]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const arr = s.split('');
    let total = 0;
    for (let i = arr.length - 1; i >= 0; i--) {
        total = (total + shifts[i]) % 26;
        arr[i] = String.fromCharCode((arr[i].charCodeAt(0) - 97 + total) % 26 + 97);
    }
    return arr.join('');
};
