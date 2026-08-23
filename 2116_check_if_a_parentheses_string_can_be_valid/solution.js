// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function(s, locked) {
    const n = s.length;
    if (n % 2 !== 0) return false;
    let bal = 0;
    for (let i = 0; i < n; i++) {
        if (locked[i] === '0' || s[i] === '(') bal++;
        else bal--;
        if (bal < 0) return false;
    }
    bal = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (locked[i] === '0' || s[i] === ')') bal++;
        else bal--;
        if (bal < 0) return false;
    }
    return true;
};
