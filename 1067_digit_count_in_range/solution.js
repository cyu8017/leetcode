// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

/**
 * @param {number} d
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var digitsCount = function(d, low, high) {
    function countUpto(n) {
        if (n < 0) return 0;
        const s = String(n);
        const length = s.length;
        let ans = 0;
        for (let i = 0; i < length; i++) {
            const left = i ? Number(s.slice(0, i)) : 0;
            const right = i + 1 < length ? Number(s.slice(i + 1)) : 0;
            const digit = Number(s[i]);
            const power = 10 ** (length - i - 1);
            if (d !== 0) {
                ans += left * power;
                if (digit > d) ans += power;
                else if (digit === d) ans += right + 1;
            } else {
                if (i === 0) continue;
                ans += (left - 1) * power;
                if (digit > 0) ans += power;
                else ans += right + 1;
            }
        }
        return ans;
    }
    return countUpto(high) - countUpto(low - 1);
};
