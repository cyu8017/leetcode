// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

/**
 * @param {string} num
 * @return {string}
 */
var largestPalindromic = function(num) {
    const freq = Array(10).fill(0);
    for (let i = 0; i < num.length; i++) freq[num.charCodeAt(i) - 48]++;
    let left = '';
    for (let d = 9; d >= 0; d--) {
        const pairs = Math.floor(freq[d] / 2);
        left += String(d).repeat(pairs);
        freq[d] %= 2;
    }
    let mid = '';
    for (let d = 9; d >= 0; d--) {
        if (freq[d] > 0) { mid = String(d); break; }
    }
    if (left.length === 0) return mid === '' ? '0' : mid;
    if (left[0] === '0') return mid === '' ? '0' : mid;
    return left + mid + left.split('').reverse().join('');
};
