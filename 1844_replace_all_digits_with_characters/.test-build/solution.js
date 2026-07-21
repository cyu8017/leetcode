"use strict";
// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/
function replaceDigits(s) {
    const chars = s.split('');
    for (let i = 1; i < chars.length; i += 2) {
        chars[i] = String.fromCharCode(chars[i - 1].charCodeAt(0) + Number(chars[i]));
    }
    return chars.join('');
}
