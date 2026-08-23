// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

/**
 * @param {number} n
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var nthMagicalNumber = function(n, a, b) {
    const MOD = 1000000007;
    const gcd = (x, y) => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    const lcm = Math.floor(a / gcd(a, b)) * b;
    let lo = 1, hi = n * Math.min(a, b);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (Math.floor(mid / a) + Math.floor(mid / b) - Math.floor(mid / lcm) >= n) hi = mid;
        else lo = mid + 1;
    }
    return lo % MOD;
};
