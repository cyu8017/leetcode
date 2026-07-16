// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    const ugly = [1];
    let index2 = 0;
    let index3 = 0;
    let index5 = 0;
    while (ugly.length < n) {
        const nextUgly = Math.min(
            ugly[index2] * 2,
            ugly[index3] * 3,
            ugly[index5] * 5,
        );
        ugly.push(nextUgly);
        if (nextUgly === ugly[index2] * 2) {
            index2 += 1;
        }
        if (nextUgly === ugly[index3] * 3) {
            index3 += 1;
        }
        if (nextUgly === ugly[index5] * 5) {
            index5 += 1;
        }
    }
    return ugly[ugly.length - 1];
};
