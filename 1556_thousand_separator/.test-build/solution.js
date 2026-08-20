"use strict";
// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/
// @ts-nocheck
function thousandSeparator(n) {
    let s = String(n);
    const parts = [];
    while (s) {
        parts.push(s.slice(-3));
        s = s.slice(0, -3);
    }
    return parts.reverse().join(".");
}
