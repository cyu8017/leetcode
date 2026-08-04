// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

/**
 * @param {number} k
 * @param {number} digit1
 * @param {number} digit2
 * @return {number}
 */
var findInteger = function(k, digit1, digit2) {
    const digits = [...new Set([digit1, digit2])].sort((a, b) => a - b);
    const q = [];
    const seen = new Set();
    for (const d of digits) {
        if (d !== 0) {
            q.push(d);
            seen.add(d);
        }
    }
    if (!q.length) return -1;
    const LIMIT = 2147483647;
    for (let qi = 0; qi < q.length; qi++) {
        const x = q[qi];
        if (x > k && x % k === 0) return x;
        for (const d of digits) {
            const nx = x * 10 + d;
            if (nx <= LIMIT && !seen.has(nx)) {
                seen.add(nx);
                q.push(nx);
            }
        }
    }
    return -1;
};
