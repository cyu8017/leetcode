// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

/**
 * @param {number} n
 * @return {number}
 */
var rotatedDigits = function(n) {
    let count = 0;
    for (let num = 1; num <= n; num++) {
        const s = String(num);
        let ok = true, changed = false;
        for (const ch of s) {
            if (ch === '3' || ch === '4' || ch === '7') { ok = false; break; }
            if (ch === '2' || ch === '5' || ch === '6' || ch === '9') changed = true;
        }
        if (ok && changed) count++;
    }
    return count;
};
