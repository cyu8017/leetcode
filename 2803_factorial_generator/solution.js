// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

/**
 * @param {number} n
 * @yields {number}
 */
var factorialGenerator = function*(n) {
    let cur = 1;
    for (let i = 1; i <= n; i++) {
        cur *= i;
        yield cur;
    }
};
