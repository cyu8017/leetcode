"use strict";
// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/
function numDupDigitsAtMostN(n) {
    const digits = String(n).split('').map(Number);
    const m = digits.length;
    const p = (a, b) => {
        let res = 1;
        for (let i = 0; i < b; i++)
            res *= a - i;
        return res;
    };
    let totalUnique = 0;
    for (let length = 1; length < m; length++) {
        totalUnique += 9 * p(9, length - 1);
    }
    const used = new Set();
    let broken = false;
    for (let i = 0; i < m; i++) {
        const d = digits[i];
        for (let x = i === 0 ? 1 : 0; x < d; x++) {
            if (used.has(x))
                continue;
            totalUnique += p(9 - i, m - i - 1);
        }
        if (used.has(d)) {
            broken = true;
            break;
        }
        used.add(d);
    }
    if (!broken)
        totalUnique += 1;
    return n - totalUnique;
}
