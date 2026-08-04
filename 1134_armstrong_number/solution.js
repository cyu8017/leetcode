// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

/**
 * @param {number} n
 * @return {boolean}
 */
var isArmstrong = function(n) {
    const digits = String(n);
    const power = digits.length;
    let sum = 0;
    for (const d of digits) sum += Number(d) ** power;
    return n === sum;
};
