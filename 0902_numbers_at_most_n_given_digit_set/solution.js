// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

/**
 * @param {string[]} digits
 * @param {number} n
 * @return {number}
 */
var atMostNGivenDigitSet = function(digits, n) {
    const k = digits.length;
    const ipow = (bas, exp) => {
        let r = 1;
        while (exp-- > 0) r *= bas;
        return r;
    };
    const countUpTo = (t) => {
        if (t.length === 0) return 0;
        let first = 0;
        for (const d of digits) if (d[0] < t[0]) first++;
        let ways = first * ipow(k, t.length - 1);
        let found = false;
        for (const d of digits) {
            if (d[0] === t[0]) {
                found = true;
                break;
            }
        }
        if (found) ways += countUpTo(t.slice(1));
        return ways;
    };
    const s = String(n);
    const m = s.length;
    let ans = 0;
    for (let i = 1; i < m; i++) ans += ipow(k, i);
    ans += countUpTo(s);
    return ans;
};
