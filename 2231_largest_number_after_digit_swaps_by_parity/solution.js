// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

/**
 * @param {number} num
 * @return {number}
 */
var largestInteger = function(num) {
    const digits = String(num).split('').map(Number);
    const even = [], odd = [];
    for (const d of digits) {
        if (d % 2 === 0) even.push(d);
        else odd.push(d);
    }
    even.sort((a, b) => b - a);
    odd.sort((a, b) => b - a);
    let ei = 0, oi = 0, ans = 0;
    for (const d of digits) {
        if (d % 2 === 0) ans = ans * 10 + even[ei++];
        else ans = ans * 10 + odd[oi++];
    }
    return ans;
};
