// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

/**
 * @param {number} divisor1
 * @param {number} divisor2
 * @param {number} uniqueCnt1
 * @param {number} uniqueCnt2
 * @return {number}
 */
var minimizeSet = function(divisor1, divisor2, uniqueCnt1, uniqueCnt2) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const lcm = Math.floor(divisor1 / gcd(divisor1, divisor2)) * divisor2;
    const ok = (x) => {
        const a = x - Math.floor(x / divisor1);
        const b = x - Math.floor(x / divisor2);
        const both = x - Math.floor(x / lcm);
        return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1 + uniqueCnt2;
    };
    let lo = 1, hi = 2 ** 62;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
