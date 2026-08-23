// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    const diff = Array(n + 1).fill(0);
    for (const sh of shifts) {
        const d = sh[2] === 0 ? -1 : 1;
        diff[sh[0]] += d;
        diff[sh[1] + 1] -= d;
    }
    const arr = s.split('');
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur = (cur + diff[i]) % 26;
        if (cur < 0) cur += 26;
        arr[i] = String.fromCharCode(97 + (arr[i].charCodeAt(0) - 97 + cur) % 26);
    }
    return arr.join('');
};
