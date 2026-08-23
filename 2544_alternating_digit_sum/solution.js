// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

/**
 * @param {number} n
 * @return {number}
 */
var alternateDigitSum = function(n) {
    const digits = [];
    let x = n;
    while (x > 0) {
        digits.push(x % 10);
        x = Math.floor(x / 10);
    }
    let ans = 0, sign = 1;
    for (let i = digits.length - 1; i >= 0; --i) {
        ans += sign * digits[i];
        sign = -sign;
    }
    return ans;
};
