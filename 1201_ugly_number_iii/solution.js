// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

/**
 * @param {number} n
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var nthUglyNumber = function(n, a, b, c) {
    const gcd = (x, y) => { while (y) { [x, y] = [y, x % y]; } return x; };
    const lcm = (x, y) => Math.floor(x / gcd(x, y)) * y;
    const ab = lcm(a, b), ac = lcm(a, c), bc = lcm(b, c), abc = lcm(ab, c);
    const count = (x) => Math.floor(x / a) + Math.floor(x / b) + Math.floor(x / c) - Math.floor(x / ab) - Math.floor(x / ac) - Math.floor(x / bc) + Math.floor(x / abc);
    let lo = 1, hi = 2000000000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (count(mid) >= n) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
