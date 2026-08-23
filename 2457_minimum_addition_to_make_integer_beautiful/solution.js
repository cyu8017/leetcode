// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var makeIntegerBeautiful = function(n, target) {
    const digitSum = (x) => {
        let s = 0;
        while (x > 0) {
            s += x % 10;
            x = Math.floor(x / 10);
        }
        return s;
    };
    const orig = n;
    let pow10 = 1;
    while (digitSum(n) > target) {
        n = Math.floor(n / 10) + 1;
        pow10 *= 10;
    }
    return n * pow10 - orig;
};
