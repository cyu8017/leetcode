// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
    return gcd(Math.min(...nums), Math.max(...nums));
};
